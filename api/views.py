from django.shortcuts import render
from .models import Donator, Pacient, Receiver

def index(request):
    return render(request, 'api/index.html')

def data(request):
    return render(request, 'api/data.html')

def panel(request):
    return render(request, 'api/panel.html')

def donators(request):
    donators = Donator.objects.all()
    return render(request, 'api/donators.html', {'donators': donators})

def pacients(request):
    pacients = Pacient.objects.all()
    return render(request, 'api/pacients.html', {'pacients': pacients})

def receivers(request):
    receivers = Receiver.objects.all()
    return render(request, 'api/receivers.html', {'receivers': receivers})