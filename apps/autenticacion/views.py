from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, authenticate
from django.contrib.auth import	login, authenticate, logout 
from apps.autenticacion.forms import LoginForms, FormularioRegistro
from django.contrib.auth.decorators import login_required, permission_required
from django.views.decorators.csrf import csrf_protect

# Create your views here.
def nuevo_usuario(request):
    if request.method == 'POST':
        formulario = FormularioRegistro(request.POST)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('/index/')
        else:
            return HttpResponseRedirect('/')
    else:
        formulario = FormularioRegistro()
        return render_to_response('autenticacion/nuevo_usuario.html', {'formulario':formulario}, context_instance = RequestContext(request))

@csrf_protect
def iniciar_sesion(request):
    mensaje = ""
    if request.user.is_authenticated():
        return HttpResponseRedirect('/')
    else:
        if request.method == "POST":
            form = LoginForms(request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password1']
                usuario = authenticate(username=username, password=password)
                if usuario is not None and usuario.is_active:
                    login(request, usuario)
                    return HttpResponseRedirect('/index/')
                else:
                    mensaje = 'Disculpa, el Nombre de Usuario o la Clave no coinciden.'
        form = LoginForms()
        ctx = {'form':form, 'mensaje':mensaje}
        return render_to_response ('autenticacion/login.html', ctx, context_instance=RequestContext(request))      

def index(request):
    return render_to_response('index.html', context_instance = RequestContext(request))

@login_required(login_url = '/')
def cerrar_sesion(request):
	logout(request)
	return HttpResponseRedirect('/')
