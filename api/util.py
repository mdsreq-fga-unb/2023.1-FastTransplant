from .models import Donator, Receiver, Log
from io import BytesIO
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.http import HttpResponse
import PyPDF2
import re
import datetime

def new_log(page, description, user):
    Log.objects.create(
        page=page,
        description=description,
        user=user
    ).save()

def read_donator_pdf():
    pass

def check_compatibility(donators, receivers):
    if donators == "all":
        dons = Donator.objects.all()
        rec = Receiver.objects.get(id=receivers)
        return [{"donator": don, "receiver": rec, "compat": don.abo == rec.abo} for don in dons]
    elif receivers == "all":
        don = Donator.objects.get(id=donators)
        recs = Receiver.objects.all()
        return [{"donator": don, "receiver": rec, "compat": don.abo == rec.abo} for rec in recs]
    else:
        don = Donator.objects.get(id=donators)
        rec = Receiver.objects.get(id=receivers)
        return [{"donator": don, "receiver": rec, "compat": don.abo == rec.abo}]

def render_to_pdf(template_src, context_dict={}):
	template = get_template(template_src)
	html  = template.render(context_dict)
	result = BytesIO()
	pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
	if not pdf.err:
		return HttpResponse(result.getvalue(), content_type='application/pdf')
	return None

def donator_pdf_to_text(file):
        read_pdf = PyPDF2.PdfReader(file)
        page = read_pdf.pages[0]
        page_content = page.extract_text()
        parsed = ""

        parsed = ''.join(page_content)
        parsed = re.sub('n', '', parsed)


        correspondencia_localidade = re.search(r'Hosp. Notificate: (\w+)', parsed)
        if correspondencia_localidade:
            localidade = correspondencia_localidade.group(1)
            # print("Localidade encontrada:", localidade)
        else:
            localidade = ""

        correspondencia_data = re.search(r'Data: (\d{2}/\d{2}/\d{4})', parsed)
        if correspondencia_data:
            data_oferta = datetime.datetime.strptime(correspondencia_data.group(1), '%d/%m/%Y').date()
            # print("Data da Oferta encontrada:", data_oferta)
        else:
            data_oferta = ""


        correspondencia_rgct = re.search(r'RGCT :(\w+-\w+)', parsed)
        if correspondencia_rgct:
            rgct = correspondencia_rgct.group(1)
            # print("RGCT encontrado:", rgct)
        else:
            rgct = ""

        correspondencia_idade = re.search(r'Idade:(\s+)(\w+)', parsed)
        if correspondencia_idade:
            idade = correspondencia_idade.group(2)
            # print("Idade encontrada:", idade)
        else:
            idade = ""


        correspondencia_sexo = re.search(r'Sexo: (\w+)', parsed)
        if correspondencia_sexo:
            sexo = correspondencia_sexo.group(1)
            # print("Sexo encontrado:", sexo)
        else:
            sexo = ""


        correspondencia_peso = re.search(r'Peso: (\d+),00', parsed)
        if correspondencia_peso:
            peso = correspondencia_peso.group(1)
            # print("Peso encontrado:", peso)
        else:
            altura = ""


        correspondencia_altura = re.search(r'Altura: (\d+) cm', parsed)
        if correspondencia_altura:
            altura = correspondencia_altura.group(1)
            # print("Altura encontrada:", altura)
        else:
            altura = ""


        correspondencia_opo = re.search(r'OPO(\s+)(\w+\s+\w+)', parsed)
        if correspondencia_opo:
            opo = correspondencia_opo.group(2)
            # print("OPO encontrado:", opo)
        else:
            opo = ""


        correspondencia_causa = re.search(r'Causa da morte ecefálica: (\w+)', parsed)
        if correspondencia_causa:
            causa_obito = correspondencia_causa.group(1)
            # print("Causa do Óbito encontrada:", causa_obito)
        else:
            causa_obito = ""

        data  = {
            "date": data_oferta,
            "location": localidade,
            "height": altura,
            "age": idade,
            "gender": sexo,
            "rgct": rgct,
            "death_cause": causa_obito,
        }
        return data