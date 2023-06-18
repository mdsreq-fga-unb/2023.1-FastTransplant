from django.shortcuts import render, redirect
from .forms import OrganForm, PacientForm, UserForm
from .models import Organ, Pacient, User

# Organ CRUD
def create_organ(request):
    if request.method == "POST":
        form = OrganForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            form = OrganForm()
    return render(request, 'create_organ.html', {'form': form})

def organ_list(request):
    organs = Organ.objects.all()
    return render(request, 'organ_list.html', {'organs': organs})

def update_organ(request, pk):
    organ = Organ.objects.get(pk=pk)
    if request.method == "POST":
        form = OrganForm(request.POST, instance=organ)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            form = OrganForm(instance=organ)
    return render(request, 'update_organ.html', {'form': form})

def delete_organ(request, pk):
    organ = Organ.objects.get(pk=pk)
    organ.delete()
    return redirect('home')

# Pacient CRUD
def create_pacient(request):
    if request.method == "POST":
        form = PacientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            form = PacientForm()
    return render(request, 'create_pacient.html', {'form': form})

def pacient_list(request):
    pacients = Pacient.objects.all()
    return render(request, 'pacient_list.html', {'pacients': pacients})

def update_pacient(request, pk):
    pacient = Pacient.objects.get(pk=pk)
    if request.method == "POST":
        form = PacientForm(request.POST, instance=pacient)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            form = PacientForm(instance=pacient)
    return render(request, 'update_pacient.html', {'form': form})

def delete_pacient(request, pk):
    pacient = Pacient.objects.get(pk=pk)
    pacient.delete()
    return redirect('home')