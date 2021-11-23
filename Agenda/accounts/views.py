from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.core.validators import validate_email
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import FormContato

# Create your views here.
def login(request):
    if request.method != "POST":
        return render(request, 'accounts/login.html')
    
    usuario = request.POST.get('usuario')
    senha = request.POST.get('senha')

    user = auth.authenticate(request, username=usuario, password=senha)
    
    if not user:
        messages.error(request, 'Usuário ou Senha inválidos')
        return render(request, 'accounts/login.html')
        
    else:
        auth.login(request, user)
        messages.success(request, 'Login efetuado com Sucesso')
        return redirect('dashboard')    
    

def logout(request):
    auth.logout(request)
    return redirect('dashboard')

@login_required(redirect_field_name='login')
def dashboard(request):
    if request.method != "POST":
        form = FormContato()
        return render(request, 'accounts/dashboard.html',{
        'form' : form
    })
        
    form = FormContato(request.POST, request.FILES)
    if not form.is_valid():
        messages.add_message(request, messages.ERROR, 'Preencha com valores válidos')
        form = FormContato(request.POST)
        return render(request, 'accounts/dashboard.html',{
        'form' : form
    })
    
       
    form.save()
    messages.add_message(request, messages.SUCCESS, 'Contato cadastrado com Sucesso!')
    return redirect('dashboard')


def cadastro(request):
    if request.method != "POST":
        return render(request, 'accounts/cadastro.html')
    
    nome = request.POST.get('nome')
    sobrenome = request.POST.get('sobrenome')
    email = request.POST.get('email')
    usuario = request.POST.get('usuario')
    senha = request.POST.get('senha')
    senha2 = request.POST.get('senha2')
    
    if not nome or not sobrenome or not email or not senha or not senha2:
        messages.add_message(request, messages.ERROR, 'Um dos campos está vázio')
        return render(request, 'accounts/cadastro.html')
    
    try:
        validate_email(email)
        
    except:
        messages.add_message(request, messages.ERROR, 'Digite um email válido')
        return render(request, 'accounts/cadastro.html')
    
    if len(senha) < 6:
        messages.add_message(request, messages.ERROR, 'Senha precisa ter mais de 6 digitos')
        return render(request, 'accounts/cadastro.html')
    
    if len(usuario) < 8:
        messages.add_message(request, messages.ERROR, 'Usuário precisa ter mais de 8 digitos')
        return render(request, 'accounts/cadastro.html')
    
    if senha != senha2:
        messages.add_message(request, messages.ERROR, 'As senhas não conferem')
        return render(request, 'accounts/cadastro.html')
    
    if User.objects.filter(username=usuario).exists():
        messages.add_message(request, messages.ERROR, 'Usuário já cadastrado')
        return render(request, 'accounts/cadastro.html')
        
    if User.objects.filter(email=email).exists():
        messages.add_message(request, messages.ERROR, 'Email já cadastrado')
        return render(request, 'accounts/cadastro.html')
        
        
    
    
    user = User.objects.create_user(username=usuario, email=email, password=senha, first_name=nome, last_name=sobrenome)
    user.save()
    messages.add_message(request, messages.SUCCESS, 'Cadastro feito com Sucesso!')
    
    return redirect('login')
