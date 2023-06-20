import datetime
import PyPDF2
import spacy
import re


from django.shortcuts import render, redirect, get_object_or_404
from .models import Donator, Patient, Receiver, OrganReport
from .forms import DonatorForm, PatientForm, ReceiverForm, OrganReportForm
from dateutil import parser as date_parser


# Carregar o modelo de linguagem em português do spaCy
nlp = spacy.load('pt_core_news_sm')

def index(request):
    return render(request, 'api/index.html')

def data(request):
    return render(request, 'api/data.html')

def panel(request):
    return render(request, 'api/panel.html')

# Donator CRUD
def donator_create(request):
    if request.method == 'POST':
        form = DonatorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_donator')
    else:
        form = DonatorForm()
    return render(request, 'api/create_donator.html', {'form': form})
        
def donator_list(request):
    donators = Donator.objects.all()
    return render(request, 'api/donators.html', {'donators': donators})

def donator_detail(request, pk):
    car = get_object_or_404(Donator, pk=pk)
    return render(request, 'donator/donator_detail.html', {'car': car})

def donator_update(request, pk):
    donator = get_object_or_404(Donator, pk=pk)
    if request.method == 'POST':
        form = DonatorForm(request.POST, instance=donator)
        if form.is_valid():
            form.save()
            return redirect('donator', pk=donator.pk)
    else:
        form = DonatorForm(instance=donator)
    return render(request, 'donator/donator_form.html', {'form': form})

def donator_delete(request, pk):
    donator = get_object_or_404(Donator, pk=pk)
    if request.method == 'POST':
        donator.delete()
        return redirect('donator')
    return render(request, 'donator/donator_confirm_delete.html', {'donator': donator})

# CRUD Patient
def patient_create(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_patient')
    else:
        form = PatientForm()
    return render(request, 'api/patient_create.html', {'form': form})
        
def patient_list(request):
    patients = Patient.objects.all()
    return render(request, 'api/patients.html', {'patients': patients})

def patient_detail(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    return render(request, 'patient/patient_detail.html', {'patient': patient})

def patient_update(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    if request.method == 'POST':
        form = PatientForm(request.POST, instance=patient)
        if form.is_valid():
            form.save()
            return redirect('patient', pk=patient.pk)
    else:
        form = PatientForm(instance=patient)
    return render(request, 'patient/patient_form.html', {'form': form})

def patient_delete(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    if request.method == 'POST':
        patient.delete()
        return redirect('patient')
    return render(request, 'patient/patient_confirm_delete.html', {'patient': patient})

# Receiver CRUD
def receiver_create(request):
    if request.method == 'POST':
        form = ReceiverForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_receiver')
    else:
        form = ReceiverForm()
    return render(request, 'api/create_receiver.html', {'form': form})
        
def receiver_list(request):
    receivers = Receiver.objects.all()
    return render(request, 'api/receivers.html', {'receivers': receivers})

def receiver_detail(request, pk):
    receiver = get_object_or_404(Receiver, pk=pk)
    return render(request, 'receiver/receiver_detail.html', {'receiver': receiver})

def receiver_update(request, pk):
    receiver = get_object_or_404(Receiver, pk=pk)
    if request.method == 'POST':
        form = ReceiverForm(request.POST, instance=receiver)
        if form.is_valid():
            form.save()
            return redirect('receiver', pk=receiver.pk)
    else:
        form = ReceiverForm(instance=receiver)
    return render(request, 'receiver/receiver_form.html', {'form': form})

def receiver_delete(request, pk):
    receiver = get_object_or_404(Receiver, pk=pk)
    if request.method == 'POST':
        receiver.delete()
        return redirect('receiver')
    return render(request, 'receiver/receiver_confirm_delete.html', {'receiver': receiver})

# Functions related to file upload
def upload_report(request):
    if request.method == 'POST':
        form = OrganReportForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('report_list')
    else:
        form = OrganReportForm()
    return render(request, 'api/index.html', {'form': form})


def upload_pdf(request):
    if request.method == 'POST' and request.FILES['pdfFile']:
        pdf_file = request.FILES['pdfFile']

        read_pdf = PyPDF2.PdfReader(pdf_file)

        number_of_pages = len(read_pdf.pages)

        page = read_pdf.pages[0]

        page_content = page.extract_text()

        parsed = ""

        # faz a junção das linhas 
        parsed = ''.join(page_content)

        # remove as quebras de linha
        parsed = re.sub('n', '', parsed)
        print("Após eliminar as quebras")
        print(parsed)

        # Extrair Nome
        #correspondencia_nome = re.search(r'Nome:(\s+)(\w+)', parsed)
        #if correspondencia_nome:
            #nome = correspondencia_nome.group(2)
            #print("Nome encontrado:", nome)
        #else:
            #nome = ""


        # Extrair Localidade
        correspondencia_localidade = re.search(r'Hosp. Notificate: (\w+)', parsed)
        if correspondencia_localidade:
            localidade = correspondencia_localidade.group(1)
            print("Localidade encontrada:", localidade)
        else:
            localidade = ""
        #donator = Donator()
        #donator.save_localidade(localidade)

        # Extrair Data da Oferta
        correspondencia_data = re.search(r'Data: (\d{2}/\d{2}/\d{4})', parsed)
        if correspondencia_data:
            data_oferta = datetime.datetime.strptime(correspondencia_data.group(1), '%d/%m/%Y').date()
            print("Data da Oferta encontrada:", data_oferta)
        else:
            data_oferta = ""
        #donator.save_data_oferta(data_oferta)

        # Extrair RGCT
        correspondencia_rgct = re.search(r'RGCT :(\w+-\w+)', parsed)
        if correspondencia_rgct:
            rgct = correspondencia_rgct.group(1)
            print("RGCT encontrado:", rgct)
        else:
            rgct = ""
        #donator.save_rgct(rgct)

        # Extrair Idade
        correspondencia_idade = re.search(r'Idade:(\s+)(\w+)', parsed)
        if correspondencia_idade:
            idade = correspondencia_idade.group(2)
            print("Idade encontrada:", idade)
        else:
            idade = ""
        #donator.save_idade(idade)

        # Extrair Sexo
        correspondencia_sexo = re.search(r'Sexo: (\w+)', parsed)
        if correspondencia_sexo:
            sexo = correspondencia_sexo.group(1)
            print("Sexo encontrado:", sexo)
        else:
            sexo = ""
        #donator.save_sexo(sexo)

        # Extrair Peso
        correspondencia_peso = re.search(r'Peso: (\d+),00', parsed)
        if correspondencia_peso:
            peso = correspondencia_peso.group(1)
            print("Peso encontrado:", peso)
        else:
            altura = ""
        #donator.save_peso(peso)

        # Extrair Altura
        correspondencia_altura = re.search(r'Altura: (\d+) cm', parsed)
        if correspondencia_altura:
            altura = correspondencia_altura.group(1)
            print("Altura encontrada:", altura)
        else:
            altura = ""
        #donator.save_altura(altura)

         # Extrair OPO
        correspondencia_opo = re.search(r'OPO(\s+)(\w+\s+\w+)', parsed)
        if correspondencia_opo:
            opo = correspondencia_opo.group(2)
            print("OPO encontrado:", opo)
        else:
            opo = ""
        #donator.save_opo(opo)

        # Extrair Causa do Óbito
        correspondencia_causa = re.search(r'Causa da morte ecefálica: (\w+)', parsed)
        if correspondencia_causa:
            causa_obito = correspondencia_causa.group(1)
            print("Causa do Óbito encontrada:", causa_obito)
        else:
            causa_obito = ""
        #donator.save_causa_obito(causa_obito)

        dados_report = OrganReport.objects.create(file=parsed)

        dados = Donator.objects.create(report=dados_report,opo=opo, rgct=rgct, date=data_oferta, location=localidade, height=altura, age=idade, gender=sexo, death_cause=causa_obito)
        dados.save()

        teste = Donator.objects.filter(opo=opo).first()
        print(teste.date)

        last_donator = Donator.objects.filter(opo=opo, rgct=rgct, date=data_oferta, location=localidade, height=altura, age=idade, gender=sexo, death_cause=causa_obito).last()
        last_opo = last_donator.opo
        last_rgct = last_donator.rgct
        last_date = last_donator.date
        last_location = last_donator.location
        last_height = last_donator.height
        last_age = last_donator.age
        last_gender = last_donator.gender
        last_death_cause = last_donator.death_cause


        return render(request, 'api\create_donator.html',  {'last_rgct': last_rgct,
                                                            'last_opo': last_opo,
                                                            'last_date': last_date,
                                                            'last_location': last_location,
                                                            'last_height': last_height,
                                                            'last_age': last_age,
                                                            'last_gender': last_gender,
                                                            'last_death_cause': last_death_cause})


    
    return render(request, 'api/donators.html')

           #dados = Donator.objects.filter(name="ana")
            #dados.update(name="ANA BEATRIZ MASSUH")
            #dados.delete()
    
def dados_receptores(request):
    if request.method == 'POST' and request.FILES['pdfFile']:
        pdf_file = request.FILES['pdfFile']

        read_pdf = PyPDF2.PdfReader(pdf_file)

        number_of_pages = len(read_pdf.pages)

        page = read_pdf.pages[0]

        page_content = page.extract_text()

        parsed = ""

        # faz a junção das linhas 
        parsed = ''.join(page_content)

        # remove as quebras de linha
        parsed = re.sub('n', '', parsed)
        print("Após eliminar as quebras")
        
        print(parsed)

        pattern = r'(\d+\s+\d+-\d+\s+[A-Za-z]+\s+[A-Za-z]+\s+[A-Za-z\s]+\s+HUB\s+-\s+Pedro\s+Rico\s+Citra)'
        matches= re.findall(pattern, parsed)

        # Process and print the extracted information
        if matches:
            match = matches[0]
            rgct = match[0].split()[1]
            name = match[1]
            abo = match[0].split()[-3]
            age = match[0].split()[-2]
            panel = match[0].split()[-1]
            print(f"RGCT: {rgct}, Name: {name}, ABO: {abo}, Age: {age}, Panel: {panel}")
        else:
            print("No match found.")

    
        #dados_report = OrganReport.objects.create(file=pdf)

        #dados = Receiver.objects.create(name=nome, rgct=rgct, abo=abo, age=idade, panel=painel, position=posicao)
        #dados.save()
                    

        return render(request, 'api/receivers.html')


    
    return render(request, 'api/index.html')


    





# def my_view(request):
    
#     last_donator = Donator.objects.filter(id=id).latest()
#     last_rgct = last_donator.rgct

#     print(id)
#     print(last_donator)

#     return render(request, 'api/create_donator.html', {'last_rgct': last_rgct})

def recep(request):


    if request.method == 'POST':
        # Obtenha os valores enviados pelo formulário
        nome = request.POST['name']
        rgct = request.POST['rgct']
        posicao = request.POST['position']
        abo = request.POST['abo']
        idade = request.POST['age']
        painel = request.POST['panel']

        dados = Receiver.objects.create(
            name=nome,
            rgct=rgct,
            position=posicao,
            abo=abo,
            age=idade,
            panel=painel,
        )
        dados.save()
            

    return render(request, 'api/donators.html')

def atualizar_dados(request):


    if request.method == 'POST':
        # Obtenha os valores enviados pelo formulário
        rgct = request.POST['rgct']
        date_string = request.POST['date']
        parsed_date = date_parser.parse(date_string)
        formatted_date = parsed_date.strftime('%Y-%m-%d')
        location = request.POST['location']
        opo = request.POST['opo']
        height = request.POST['height']
        age = request.POST['age']
        gender = request.POST['gender']
        death_cause = request.POST['death_cause']

        # Obtenha o último donator
        last_donator = Donator.objects.last()

        # Verifique se o último donator existe e possui um report associado
        if last_donator and last_donator.report:
            # Use o report do último donator para criar o novo donator
            dados = Donator.objects.create(
                report=last_donator.report,
                rgct=rgct,
                date=formatted_date,
                location=location,
                opo=opo,
                height=height,
                age=age,
                gender=gender,
                death_cause=death_cause
            )
            dados.save()
            print('Atualização de dados:')
            print(rgct)
            print(formatted_date)
            print(location)
            print(opo)
            print(height)
            print(age)
            print(gender)
            print(death_cause)
        else:
            print('Não foi possível encontrar um report válido para associar ao donator.')

    return render(request, 'api/receivers.html')
