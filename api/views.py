import PyPDF2
import spacy
import re

from django.shortcuts import render, redirect, get_object_or_404
from .models import Donator, Patient, Receiver, OrganReport
from .forms import DonatorForm, PatientForm, ReceiverForm, OrganReportForm

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

        # Extrair RGCT
        correspondencia_rgct = re.search(r'RGCT:(\w+-\w+)', parsed)
        if correspondencia_rgct:
            rgct = correspondencia_rgct.group(1)
            print("RGCT encontrado:", rgct)
        else:
            rgct = ""

        # Extrair Data da Oferta
        correspondencia_data = re.search(r'Data:(\d{2}/\d{2}/\d{4})', parsed)
        if correspondencia_data:
            data_oferta = correspondencia_data.group(1)
            print("Data da Oferta encontrada:", data_oferta)
        else:
            data_oferta = ""
        
        # Extrair Localidade
        correspondencia_localidade = re.search(r'Hosp\. Notificante:(\w+)', parsed)
        if correspondencia_localidade:
            localidade = correspondencia_localidade.group(1)
            print("Localidade encontrada:", localidade)
        else:
            localidade = ""

        # Extrair OPO
        correspondencia_opo = re.search(r'OPO(\s+)(\w+\s+\w+)', parsed)
        if correspondencia_opo:
            opo = correspondencia_opo.group(2)
            print("OPO encontrado:", opo)
        else:
            opo = ""

        # Extrair Altura
        correspondencia_altura = re.search(r'Altura:(\d+)\scm', parsed)
        if correspondencia_altura:
            altura = correspondencia_altura.group(1)
            print("Altura encontrada:", altura)
        else:
            altura = ""

        # Extrair Idade
        correspondencia_idade = re.search(r'Idade:(\s+)(\w+)', parsed)
        if correspondencia_idade:
            idade = correspondencia_idade.group(2)
            print("Idade encontrada:", idade)
        else:
            idade = ""

        # Extrair Sexo
        correspondencia_sexo = re.search(r'Sexo:(\w+)', parsed)
        if correspondencia_sexo:
            sexo = correspondencia_sexo.group(1)
            print("Sexo encontrado:", sexo)
        else:
            sexo = ""

        # Extrair Causa do Óbito
        correspondencia_causa = re.search(r'Causa da morte encefálica:(\w+)', parsed)
        if correspondencia_causa:
            causa_obito = correspondencia_causa.group(1)
            print("Causa do Óbito encontrada:", causa_obito)
        else:
            causa_obito = ""

        return render(request, 'api/confirmation.html', {'pdf_file_name': pdf_file.name})
    
    return render(request, 'api/patients.html')