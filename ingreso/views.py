from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def index (request):
    if request.method == 'GET':
        return render(request, "home.html", {'form' : AuthenticationForm})
    else:
        name = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=name, password=password)
        if user is None:
            return render(request, "home.html", {'form' : AuthenticationForm, 'error' : "Usuario y/o Password incorrecto"})
        else:
            login(request,user)
            return redirect("inicio/")

def registro(request):
    if request.method == 'GET':
        return render(request, "registro.html", { 'form' : UserCreationForm})
    else:
        if request.POST['password1']!=request.POST['password2']:
            return render(request, "registro.html", { 'form' : UserCreationForm, 'error' : "Las Contraseñas no coinciden"})
        else:
            name = request.POST['username']
            password = request.POST['password1']
            user = User.objects.create_user(username=name, password=password )
            user.save()
            return render(request, "registro.html", { 'form' : UserCreationForm, 'mensaje' : "Usuario Registrado"}) 

@login_required
def inicio(request):
    return render(request, 'inicio.html')

def salir(request):
    logout(request)
    return redirect("../")