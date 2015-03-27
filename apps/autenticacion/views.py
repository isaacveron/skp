from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, authenticate
from django.contrib.auth import	login, authenticate, logout 
from apps.autenticacion.forms import UsuarioForm, UsuarioModForm, RolForm
from django.contrib.auth.models import User, Group, Permission
from django.contrib.auth.decorators import login_required, permission_required
from django.views.decorators.csrf import csrf_protect

# Create your views here.
@csrf_protect
def iniciar_sesion(request):
    if not request.user.is_anonymous():
        return HttpResponseRedirect('/index/')
    if request.method == 'POST':
        formulario = AuthenticationForm(request.POST)
        if formulario.is_valid:
            usuario_actor = request.POST['username']
            clave = request.POST['password']
            acceso = authenticate(username=usuario_actor, password=clave)
            if acceso is not None:
                if acceso.is_active:
                    login(request, acceso)
                    return HttpResponseRedirect('/index/')
                else:
                    return render_to_response('no_activo.html', context_instance=RequestContext(request))
            else:
                return render_to_response('autenticacion/sesion_error.html', context_instance=RequestContext(request))
    else:
        formulario = AuthenticationForm()
    return render_to_response('autenticacion/login.html', {'formulario': formulario}, context_instance=RequestContext(request))

def index(request):
    return render_to_response('index.html', context_instance = RequestContext(request))

@csrf_protect
def crear_usuario(request):
    usuario_actor = request.user
    if request.method == 'POST':
        formulario = UsuarioForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            lista_usuarios = User.objects.all()
            return render_to_response('usuario/operacion_usuario_exito.html',{'mensaje': 'El usuario ha sido creado con exito', 'usuario_actor': usuario_actor,'lista_usuarios': lista_usuarios}, context_instance=RequestContext(request))
    else:
        formulario = UsuarioForm()
    return render_to_response('usuario/form_add_usuario.html',
                              {'formulario': formulario, 'operacion': 'Creacion de un nuevo usuario',
                               'usuario_actor': usuario_actor}, context_instance=RequestContext(request))

def detalle_usuario(request, id_usuario_p):
    usuario_parametro = User.objects.get(pk=id_usuario_p)
    return render_to_response('usuario/detalle_usuario.html', {'usuario_actor': request.user,'usuario_parametro': usuario_parametro}, context_instance=RequestContext(request))

def modificar_usuario(request):
    usuario_actor = request.user
    if request.method == 'POST':
        formulario = UsuarioModForm(request.POST, instance=usuario_actor)
        if formulario.is_valid():
           form = formulario.save(commit=False)
           form.user = request
           form.save()
           lista_usuarios = User.objects.all()
           return render_to_response('usuario/operacion_usuario_exito.html',
                                     {'mensaje': 'Se ha actualizado tu informacion personal', 'usuario_actor': usuario_actor,
                                      'lista_usuarios': lista_usuarios}, context_instance=RequestContext(request))
    else:
        formulario = UsuarioModForm(instance=usuario_actor)
    return render(request, 'usuario/form_mov_usuario.html',
                  {'usuario_actor': usuario_actor, 'formulario': formulario, 'operacion': 'Gestion de datos personales'},
                  context_instance=RequestContext(request))

@login_required(login_url = '/')
def cerrar_sesion(request):
    logout(request)
    return HttpResponseRedirect('/')


def crear_rol(request):
    """

    :param request:
    :return:
    """
    mensaje="Rol creado con exito"
    usuario_actor = request.user
    rol = Group(Usuario=usuario_actor)
    if request.method == 'POST':
        formulario = RolForm(request.POST, instance=rol)
        if formulario.is_valid():
            formulario.save()
            roles = Group.objects.all()
            return render_to_response('rol/crear_rol_exito.html',
                                      {'mensaje': mensaje, 'usuario_actor': usuario_actor, 'roles': roles},
                                      context_instance=RequestContext(request))
    else:
        formulario = RolForm()
    return render_to_response('rol/crear_rol.html',
                              {'formulario': formulario, 'operacion': 'Crear rol',
                               'usuario_actor': usuario_actor},
                              context_instance=RequestContext(request))
def administrar_roles(request):
    """

    :param request:
    :return:
    """
    usuario_actor = request.user
    roles = Group.objects.all()
    return render_to_response('rol/administrar_rol.html',
                              {'usuario_actor': usuario_actor, 'roles': roles}, context_instance=RequestContext(request))

def detalle_rol(request, idRol):
    """

    :param request:
    :param idRol:
    :return:
    """
    usuario_actor = request.user
    rol = Group.objects.get(pk=idRol)
    return render_to_response('rol/detallerol.html', {'usuario_actor': usuario_actor, 'rol': rol},
                              context_instance=RequestContext(request))
