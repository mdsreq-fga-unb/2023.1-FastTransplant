from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import *
from .util import *
from django.core.mail import send_mail
from django.conf import settings
from django.urls import reverse
from django.views import View
from django.contrib import messages

# 404 error handler
def error_404(request, exception):
    return render(request, 'api/404.html')

# Password recovery
def recover(request):
    if request.method == 'POST':
        email = request.POST['email']
        user = User.objects.filter(email=email).first()
        if user is not None:
            url = request.build_absolute_uri(reverse('password_reset', args=[user.username]))
            if PasswordChangeRequest.objects.filter(user=user).first() is None:
                user_request = PasswordChangeRequest.objects.create(user=user)
                user_request.save()
                send_mail("FastTransplant - Recuperação de senha",
                        f"Prezado(a) {user.first_name},\n\nVocê solicitou a recuperação de senha no sistema FastTransplant.\nClique no link abaixo para redefini-la:{url}\n\nAtenciosamente,\nEquipe 0011.",
                        "settings.EMAIL_HOST_USER",
                        [email],
                        fail_silently=False)
                messages.success(request, 'E-mail enviado com sucesso.')
            else: messages.error(request, 'E-mail já enviado.')
        else: messages.error(request, 'E-mail não cadastrado.')
        return redirect('recover')
    return render(request, 'api/recover.html')

# Login and logout
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            new_log("Index", f"{request.user.first_name} {request.user.last_name} entrou no sistema.", request.user)
            return redirect('index')
        else:
            messages.error(request, 'Usuário ou senha inválidos.')
            return redirect('login')
    else: return render(request, 'api/login.html')

def logout_view(request):
    new_log("Logout", f"{request.user.first_name} {request.user.last_name} saiu do sistema.", request.user)
    logout(request)
    return redirect('login')

# Menu Pages
@login_required(login_url='login')
def index(request):
    context = {
        'donators': Donator.objects.count(),
        'receivers': Receiver.objects.count(),
        'users': User.objects.count(),
        'acceptance': Acceptance.objects.filter(decision="Aceito").count(),
    }
    return render(request, 'api/index.html', context)

@login_required(login_url='login')
def users_list(request):
    context = {
        'users': User.objects.all(),
    }
    return render(request, 'api/users_list.html', context)

@login_required(login_url='login')
def profile(request):
    context = {
        'user': request.user,
    }
    if request.method == 'POST':
        request.user.first_name = request.POST['first_name']
        request.user.last_name = request.POST['last_name']
        request.user.email = request.POST['email']
        request.user.username = request.POST['username']
        request.user.job = request.POST['job']
        request.user.education = request.POST['education']
        request.user.location = request.POST['location']
        request.user.save()
        new_log("Perfil", f"{request.user.first_name} {request.user.last_name} atualizou seu perfil.", request.user)
        messages.success(request, 'Perfil atualizado com sucesso.')
        return redirect('profile')
    else: return render(request, 'api/profile.html', context)

@login_required(login_url='login')
def compatibility(request):
    context = {
        'available_donators': Donator.objects.all(),
        'available_receivers': Receiver.objects.all(),
    }
    if request.method == 'POST':
        donators = request.POST['donators']
        receivers = request.POST['receivers']
        context["results"] = check_compatibility(donators, receivers)
        context["selected_donator"] = donators
        context["selected_receiver"] = receivers
        return render(request, 'api/compatibility.html', context)
    else: 
        return render(request, 'api/compatibility.html', context)

@login_required(login_url='login')
def log(request):
    logs = Log.objects.all()
    if request.method == 'POST':
        logs.delete()
        messages.success(request, 'Log apagado com sucesso.')
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
        abo = request.POST['abo']
        height = request.POST['height']

        donator = Donator.objects.create(report='', rgct=rgct, age=age, gender=gender, death_cause=death_cause, date=date, location=location, abo=abo, height=height)
        donator.save()
        new_log("Doadores", f"{request.user.first_name} {request.user.last_name} registrou um novo doador.", request.user)
        messages.success(request, 'Doador cadastrado com sucesso.')
        return redirect('donators_list')
    else: return render(request, 'api/donators_form.html', {'page': 'Adicionar'})

@login_required(login_url='login')
def donators_create_pdf(request):
    if request.method == 'POST' and request.FILES['docpdf']:
        donator_file = request.FILES['docpdf']
        data = donator_pdf_to_text(donator_file)
        donator = Donator.objects.create(
            # rgct=data['rgct'],
            location=data['location'],
            height=data['height'],
            age=data['age'],
            gender=data['gender'],
            death_cause=data['death_cause'],
        )
        donator.save()
        return redirect('donators_update', id=donator.id)
        
    else: return render(request, 'api/donators_form_pdf.html')

@login_required(login_url='login')
def donators_read(request, id):
    donator = Donator.objects.get(id=id)
    new_log("Doadores", f"{request.user.first_name} {request.user.last_name} consultou os dados do doador {donator.id}.", request.user)
    return render(request, 'api/donator.html', {'donator': donator})

@login_required(login_url='login')
def donators_update(request, id):
    donator = Donator.objects.get(id=id)
    if request.method == 'POST':
        donator.rgct = request.POST['rgct']
        donator.age = request.POST['age']
        donator.gender = request.POST['gender']
        donator.date = request.POST['date']
        donator.location = request.POST['location']
        donator.abo = request.POST['abo']
        donator.height = request.POST['height']
        donator.save()
        new_log("Doadores", f"{request.user.first_name} {request.user.last_name} atualizou os dados do doador #{donator.id}.", request.user)
        messages.success(request, 'Doador atualizado com sucesso.')
        return redirect('donators_list')
    return render(request, 'api/donators_form.html', {'donator': donator, 'page': 'Atualizar'})

@login_required(login_url='login')
def donators_delete(request, id):
    donator = Donator.objects.get(id=id)
    if request.method == 'POST':
        donator.delete()
        new_log("Doadores", f"{request.user.first_name} {request.user.last_name} deletou um doador do sistema.", request.user)
        messages.success(request, 'Doador deletado com sucesso.')
        return redirect('donators_list')
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
        new_log("Receptores", f"{request.user.first_name} {request.user.last_name} registrou um novo receptor.", request.user)
        messages.success(request, 'Receptor cadastrado com sucesso.')
        return redirect('receivers_list')
    else: return render(request, 'api/receivers_form.html', {'page': 'Adicionar'})

@login_required(login_url='login')
def receivers_create_pdf(request):
    return render(request, 'api/receivers_form_pdf.html')

@login_required(login_url='login')
def receivers_read(request, id):
    receiver = Receiver.objects.get(id=id)
    new_log("Receptores", f"{request.user.first_name} {request.user.last_name} consultou os dados do receptor {receiver.id}.", request.user)
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
        new_log("Receptores", f"{request.user.first_name} {request.user.last_name} atualizou os dados do receptor #{receiver.id}.", request.user)
        messages.success(request, 'Receptor atualizado com sucesso.')
        return redirect('receivers_list')
    return render(request, 'api/receivers_form.html', {'receiver': receiver, 'page': 'Atualizar'})

@login_required(login_url='login')
def receivers_delete(request, id):
    receiver = Receiver.objects.get(id=id)
    if request.method == 'POST':
        receiver.delete()
        new_log("Receptores", f"{request.user.first_name} {request.user.last_name} deletou um receptor do sistema.", request.user)
        messages.success(request, 'Receptor deletado com sucesso.')
        return redirect('receivers_list')
    else: return render(request, 'api/receivers_delete.html', {'receiver': receiver})

def error(request):
    return render(request, 'api/404.html')

@login_required(login_url='login')
def reports(request):
    if request.method == 'POST':
        donators = request.POST.get('donators', False)
        receivers = request.POST.get('receivers', False)
        transplants = request.POST.get('transplants', False)
        users = request.POST.get('users', False)

        data = {
            "donators": Donator.objects.all() if donators else False,
            "receivers": Receiver.objects.all() if receivers else False,
            "transplants": Acceptance.objects.all() if transplants else False,
            "users": User.objects.all() if users else False,
            }
        pdf = render_to_pdf('api/pdf_template.html', data)
        new_log("Relatórios", f"{request.user.first_name} {request.user.last_name} gerou um relatório.", request.user)
        return HttpResponse(pdf, content_type='application/pdf')
    else: return render(request, 'api/reports.html')

@login_required(login_url='login')
def results(request):
    context = {
        "transplants": Acceptance.objects.all(),
    }
    if request.method == 'POST':
            pass
    else: return render(request, 'api/results.html', context)

@login_required(login_url='login')
def results_read(request, id):
    acceptance = Acceptance.objects.get(id=id)
    return render(request, 'api/results_read.html', {'acceptance': acceptance})

@login_required(login_url='login')
def users_create(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        category = request.POST['category']
        username = request.POST['username']
        user = User.objects.create_user(first_name=name, email=email, category=category, username=username, password='0011')
        user.save()
        user_request = PasswordChangeRequest.objects.create(user=user)
        user_request.save()
        new_log("Usuários", f"{request.user} registrou um novo usuário.", request.user)
        url = request.build_absolute_uri(reverse('password_reset', args=[user.username]))
        send_mail("Bem-vindo ao sistema FastTransplant!",
                f"Prezado(a) {name},\n\nVocê foi adicionado recentemente ao sistema FastTransplant.\nSeu username é: {username}\nClique no link abaixo para definir a sua senha:{url}",
                "settings.EMAIL_HOST_USER",
                [email],
                fail_silently=False)
        return redirect('users_list')
    else: return render(request, 'api/users_form.html')

def password_reset(request, username):
    context = {
        'username': request.path.split('/')[-1]
    }
    if request.method == 'POST':
        password = request.POST['password']
        password_confirm = request.POST['password_confirm']
        user = User.objects.filter(username=username).first()
        if password == password_confirm and user is not None:
            user.set_password(password)
            user.save()
            user_request = PasswordChangeRequest.objects.get(user=user)
            user_request.delete()
            new_log("Usuários", f"{user.first_name} {user.last_name} redefiniu a sua senha", user)
            messages.success(request, 'Senha redefinida com sucesso!')
            return redirect('login')
        else: 
            messages.error(request, 'As senhas não coincidem!')
            previous_page = request.META.get('HTTP_REFERER')
            return HttpResponseRedirect(previous_page)
    else: return render(request, 'api/password_reset.html', context)

@login_required(login_url='login')
def users_read(request, id):
    user = User.objects.get(id=id)
    new_log("Usuários", f"{request.user.first_name} consultou os dados do usuário #{user.id}.", request.user)
    return render(request, 'api/users_read.html', {'user': user})

@login_required(login_url='login')
def users_delete(request, id):
    user = User.objects.get(id=id)
    if request.method == 'POST':
        user.delete()
        new_log("Usuários", f"{request.user.first_name} deletou um usuário do sistema.", request.user)
        return redirect('users_list')
    else: return render(request, 'api/users_delete.html', {'user': user})

@login_required(login_url='login')
def transplant(request, donator_id, receiver_id, compatibility):
    context = {
        "donator_id": donator_id,
        "receiver_id": receiver_id,
        "compatibility": compatibility,
    }
    if request.method == 'POST':
        decision = request.POST['decision']
        description = request.POST['description']
        new_transplant = Acceptance.objects.create(
            user=request.user,
            donator=Donator.objects.filter(id=donator_id).first(),
            receiver=Receiver.objects.filter(id=receiver_id).first(),
            compatibility=compatibility,
            decision=decision,
            description=description)
        new_transplant.save()
        new_log("Compatibilidade/Transplantes", f"{request.user.first_name} {request.user.last_name} registrou um novo transplante ({decision}).", request.user)
        messages.success(request, 'Transplante registrado com sucesso!')
        return redirect('compatibility')
    else: return render(request, 'api/transplant.html', context)