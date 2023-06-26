from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *


# Create your views here.


def index(request):
    return HttpResponse("Hello, world. You're at the api index.")

# CRUD for donators
def donators_list(request):
    donators = Donator.objects.all()
    return render(request, 'donators_list.html', {'donators': donators})

def donators_create(request):
    if request.method == 'POST':
        # rgct = request.POST['rgct']
        donator = Donator.objects.create()
        donator.save()
        return redirect('donators')
    else: return render(request, 'donator_create.html')

def donators_read(request, id):
    donator = Donator.objects.get(id=id)
    return render(request, 'donator.html', {'donator': donator})

def donators_update(request, id):
    pass

def donators_delete(request, id):
    pass

# CRUD for receivers
def receivers_list(request):
    receivers = Receiver.objects.all()
    return render(request, 'receiver_list.html', {'receivers': receivers})

def receivers_create(request):
    if request.method == 'POST':
        # rgct = request.POST['rgct']
        receiver = Receiver.objects.create()
        receiver.save()
        return redirect('receivers')
    else: return render(request, 'receiver_create.html')

def receivers_read(request, id):
    receiver = Receiver.objects.get(id=id)
    return render(request, 'receiver.html', {'receiver': receiver})

def receivers_update(request, id):
    pass

def receivers_delete(request, id):
    pass

# Compatibility
def compatibility(request):
    pass

# Log
def log(request):
    logs = Log.objects.all()
    return render(request, 'log.html', {'logs': logs})