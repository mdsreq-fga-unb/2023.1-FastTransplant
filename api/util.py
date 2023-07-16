from .models import Donator, Receiver, Log
from io import BytesIO
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.http import HttpResponse

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