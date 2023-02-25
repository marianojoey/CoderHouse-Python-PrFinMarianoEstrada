from django.shortcuts import render
from ElFicticio.forms import *
from ElFicticio.models import *
from django.views.generic import *
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# Create your views here.

def v_inicioSesion(request):
    if request.method == "POST":
        form_ingreso = AuthenticationForm(request, data=request.POST)
        if form_ingreso.is_valid():
            usuario = form_ingreso.cleaned_data.get("username")
            contraseña=form_ingreso.cleaned_data.get("password")

            ingresante = authenticate(username = usuario, password = contraseña)

            if ingresante:
                login(request,ingresante)
                return render (request, 'ElFicticio/inicio.html', {"mensaje":f"Bienvenido: {ingresante}"})
            else:
                return render (request, 'ElFicticio/inicio.html', {"mensaje":"Usuario o Contraseña inválidos"})
    else:
        form_ingreso = AuthenticationForm()
    
    return render (request, "ElFicticio/login.html", {"formulario":form_ingreso})

def v_registro(request):
    if request.method == "POST":
        form_registro=FRegistro(request.POST)
        if form_registro.is_valid():
            username = form_registro.cleaned_data["username"]
            form_registro.save()
            return render (request, "ElFicticio/inicio.html", {"mensaje": "Usuario Creado"})
    else:
        form_registro= FRegistro()
    
    return render (request, "ElFicticio/registro.html", {"formulario":form_registro})

def v_inicio(request):
    return render(request,"ElFicticio/inicio.html")

@login_required
def v_notas(request):
    return render(request,"ElFicticio/notas.html")

@login_required
def v_editor(request):
    return render(request,"ElFicticio/editor.html")

def v_contacto(request):
    return render(request,"ElFicticio/contacto.html")

@login_required
def v_editar(request):
    return render(request, "ElFicticio/editar.html")

def v_inexistente(request):
    return render(request, "ElFicticio/inexistente.html")
