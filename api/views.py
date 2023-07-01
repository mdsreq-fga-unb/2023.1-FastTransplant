from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import *
from .util import new_log

# Login and logout
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            new_log("Index", f"{request.user} entrou no sistema.", request.user)
            return redirect('index')
        else: error_message = 'Usuário ou senha inválidos.'
    else: error_message = None
    return render(request, 'api/login.html', {'error_message': error_message})

def logout_view(request):
    new_log("Logout", f"{request.user} saiu do sistema.", request.user)
    logout(request)
    return redirect('login')

# Menu Pages
@login_required(login_url='login')
def index(request):
    context = {
        'donators': Donator.objects.count(),
        'receivers': Receiver.objects.count(),
    }
    return render(request, 'api/index.html', context)

@login_required(login_url='login')
def users(request):
    return render(request, 'api/users.html')

@login_required(login_url='login')
def profile(request):
    return render(request, 'api/profile.html')

@login_required(login_url='login')
def search(request):
    return render(request, 'api/search.html')

@login_required(login_url='login')
def settings(request):
    return render(request, 'api/settings.html')

@login_required(login_url='login')
def compatibility(request, donator_id, receiver_id):
    pass

@login_required(login_url='login')
def log(request):
    logs = Log.objects.all()
    if request.method == 'POST':
        logs.delete()
        return redirect('log')
    else: return render(request, 'api/log.html', {'logs': logs})

# CRUD for donators
@login_required(login_url='login')
def donators_list(request):
    donators = Donator.objects.all()
    return render(request, 'api/donators_list.html', {'donators': donators})

@login_required(login_url='login')
def donators_create(request):
    if request.method == 'POST':
        rgct = request.POST['rgct']
        age = request.POST['age']
        gender = request.POST['gender']
        death_cause = request.POST['death_cause']
        date = request.POST['date']
        location = request.POST['location']
        opo = request.POST['opo']
        height = request.POST['height']

        donator = Donator.objects.create(report='', rgct=rgct, age=age, gender=gender, death_cause=death_cause, date=date, location=location, opo=opo, height=height)
        donator.save()
        new_log("Doadores", f"{request.user} registrou um novo doador.", request.user)
        return redirect('donators_list')
    else: return render(request, 'api/donators_form.html', {'page': 'Adicionar'})

@login_required(login_url='login')
def donators_read(request, id):
    donator = Donator.objects.get(id=id)
    new_log("Doadores", f"{request.user} consultou os dados do doador {donator.id}.", request.user)
    return render(request, 'api/donator.html', {'donator': donator})

@login_required(login_url='login')
def donators_update(request, id):
    donator = Donator.objects.get(id=id)
    if request.method == 'POST':
        # donator.name = request.POST['name']
        donator.save()
        new_log("Doadores", f"{request.user} atualizou os dados do doador {donator.id}.", request.user)
        return redirect('donators')
    return render(request, 'api/donators_update.html', {'donator': donator})

@login_required(login_url='login')
def donators_delete(request, id):
    donator = Donator.objects.get(id=id)
    if request.method == 'POST':
        donator.delete()
        new_log("Doadores", f"{request.user} deletou um doador do sistema.", request.user)
        return redirect('donators')
    else: return render(request, 'api/donators_delete.html', {'donator': donator})
    
# CRUD for receivers
@login_required(login_url='login')
def receivers_list(request):
    receivers = Receiver.objects.all()
    return render(request, 'api/receivers_list.html', {'receivers': receivers})

@login_required(login_url='login')
def receivers_create(request):
    if request.method == 'POST':
        name = request.POST['name']
        rgct = request.POST['rgct']
        position = request.POST['position']
        abo = request.POST['abo']
        age = request.POST['age']
        panel = request.POST['panel']
        receiver = Receiver.objects.create(name=name, rgct=rgct, position=position, abo=abo, age=age, panel=panel)
        receiver.save()
        new_log("Receptores", f"{request.user} registrou um novo receptor.", request.user)
        return redirect('receivers_list')
    else: return render(request, 'api/receivers_form.html', {'page': 'Adicionar'})

@login_required(login_url='login')
def receivers_read(request, id):
    receiver = Receiver.objects.get(id=id)
    new_log("Receptores", f"{request.user} consultou os dados do receptor {receiver.id}.", request.user)
    return render(request, 'api/receiver.html', {'receiver': receiver})

@login_required(login_url='login')
def receivers_update(request, id):
    receiver = Receiver.objects.get(id=id)
    if request.method == 'POST':
        receiver.name = request.POST['name']
        receiver.rgct = request.POST['rgct']
        receiver.position = request.POST['position']
        receiver.abo = request.POST['abo']
        receiver.age = request.POST['age']
        receiver.panel = request.POST['panel']
        receiver.save()
        new_log("Receptores", f"{request.user} atualizou os dados do receptor #{receiver.id}.", request.user)
        return redirect('receivers_list')
    return render(request, 'api/receivers_form.html', {'receiver': receiver, 'page': 'Atualizar'})

@login_required(login_url='login')
def receivers_delete(request, id):
    receiver = Receiver.objects.get(id=id)
    if request.method == 'POST':
        receiver.delete()
        new_log("Receptores", f"{request.user} deletou um receptor do sistema.", request.user)
        return redirect('receivers_list')
    else: return render(request, 'api/receivers_delete.html', {'receiver': receiver})