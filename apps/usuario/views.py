from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, authenticate
from django.contrib.auth import	login, authenticate, logout 
from apps.usuario.forms import UsuarioForm, UsuarioModForm
from apps.roles.forms import AsignarRol
from django.contrib.auth.models import User, Group, Permission
from django.contrib.auth.decorators import login_required, permission_required
from django.views.decorators.csrf import csrf_protect

# Create your views here.
@csrf_protect
def iniciar_sesion(request):
    """
    Vista de inicio de sesion
    * Si el usuario inicia sesion con exito, retorna iniciar_sesion.html
    * Si el usuario esta inactivo, retorna no_activo.html
    * Si el usuario no exite en el sistema, retorna sesion_error.html

    * Variables
        -   formulario: es el formulario que el usuario debe completar para iniciar sesion
        -   usuario_actor: es el usuario que realiza la accion
        -   clave: es la clave secreta introducida por el usuario_actor
        -   acceso: contiene el resultado de la funcion authenticate que lleva como parametro
            el par(usuario, contrasenha) verificando su existencia y estado en el sistema
    """
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

@login_required(login_url = '/')
def index(request):
    return render_to_response('index.html', context_instance = RequestContext(request))

@login_required(login_url = '/')
def crear_usuario(request):
    """
    Vista de creacion de nuevo usuario

    Recibe como parametro un request y retorna la pagina web form_usuario.html donde se debe completar
    los datos del usuario y luego operacion_usuario_exito.html si se completo debidamente el formulario
    * Variables
        -   usuario_actor: es el usuario que realiza la accion
        -   formulario: es el fomrulario que debe completar el usuario_actor
        -   lista_usuarios: es la lista de usuarios existentes en el sistema
    """
    mensaje = "El usuario ha sido creado con exito"
    usuario_actor = request.user
    if request.method == 'POST':
        formulario = UsuarioForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            lista_usuarios = User.objects.all()
            return render_to_response('usuario/operacion_usuario_exito.html',{'mensaje': mensaje, 'usuario_actor': usuario_actor,'lista_usuarios': lista_usuarios}, context_instance=RequestContext(request))
    else:
        formulario = UsuarioForm()
    return render_to_response('usuario/form_add_usuario.html',
                              {'formulario': formulario, 'operacion': 'Creacion de un nuevo usuario',
                               'usuario_actor': usuario_actor}, context_instance=RequestContext(request))

def administrar_usuario(request):
    """

    :param request:
    :return:

    Vista de administrar usuario

    | Recibe como parametro un request y retorna la pagina web administrar_usuario.html donde se muestra
    | la lista de usuarios si el usuario_actor posee los permsos correspondientes

    * Variables
        -   usuario_actor: es el usuario que realiza la accion
        -   lista_usuarios: es la lista de usuarios existentes en el sistema
    """
    usuario_actor = request.user
    lista_usuarios = User.objects.all()
    return render_to_response('usuario/administrar_usuario.html', {'usuario_actor':usuario_actor,'lista_usuarios':lista_usuarios},
                              context_instance=RequestContext(request))

@csrf_protect
@login_required(login_url = '/')
def detalle_usuario(request, idUsuario):
    """
    Vista detalle del usuario

    Recibe un request y un id de usuario como parametro y retorna la pagina web detalle_usuario.html
    * Variables
        -usuario_parametro: es el usuario que se vera en detalle en la pagina web detalle_usuario.html
    """
    usuario_parametro = User.objects.get(pk=idUsuario)
    return render_to_response('usuario/detalle_usuario.html', {'usuario_actor': request.user,'usuario_parametro': usuario_parametro}, context_instance=RequestContext(request))


@login_required(login_url = '/')
def modificar_usuario(request, idUsuario):
    """"  
    Vista de modificacion de nuevo usuario

    Recibe como parametro un request y retorna la pagina web form_usuario.html donde se debe completar
    los datos el usuario y luego operacion_usuario_exito.html si se completo debidamente el formulario
    * Variables
        -   usuario_actor: es el usuario que realiza la accion
        -   formulario: es el fomrulario que debe completar el usuario_actor
        -   lista_usuarios: es la lista de usuarios existentes en el sistema
    """
    mensaje = "Se ha actualizado tu informacion personal"
    usuario_actor = User.objects.get(pk=idUsuario)
    if request.method == 'POST':
        formulario = UsuarioModForm(request.POST, instance=usuario_actor)
        if formulario.is_valid():
           form = formulario.save(commit=False)
           form.user = request
           form.save()
           lista_usuarios = User.objects.all()
           return render_to_response('usuario/operacion_usuario_exito.html',
                                     {'mensaje': mensaje, 'usuario_actor': usuario_actor,
                                      'lista_usuarios': lista_usuarios}, context_instance=RequestContext(request))
    else:
        formulario = UsuarioModForm(instance=usuario_actor)
    return render(request, 'usuario/form_mov_usuario.html',
                  {'usuario_actor': usuario_actor, 'formulario': formulario, 'operacion': 'Gestion de datos personales'},
                  context_instance=RequestContext(request))

def asignar_rol(request, idRol): 
    mensaje="Rol asignado con exito"
    usuario_actor = request.user
    usuario_parametro = User.objects.get(pk=idRol)
    if request.method == 'POST':
        formulario = AsignarRol(request.POST, instance=usuario_parametro)
        if formulario.is_valid():
           formulario.save()
           roles = Group.objects.all()
           return render_to_response('usuario/operacion_usuario_exito.html',{'mensaje': mensaje, 'usuario_actor': usuario_actor}, context_instance=RequestContext(request))
    else:
        formulario = AsignarRol(instance=usuario_parametro)
    return render(request, 'rol/form_rol.html', {'usuario_parametro': usuario_parametro, 'formulario': formulario,
                                                 'operacion': 'Asignacion de rol', 'usuario_actor': usuario_actor},
                  context_instance=RequestContext(request))

def vista_eliminar_usuario(request, idUsuario):
    """

    :param request:
    :param idRol:
    :return:
    """
    usuario_actor = request.user
    usuario_parametro = User.objects.get(pk=idUsuario)
    return render_to_response('usuario/eliminar_usuario.html', {'usuario_actor': usuario_actor, 'usuario_parametro': usuario_parametro},
                              context_instance=RequestContext(request))

def eliminar_usuario(request, idUsuario):
    """

    :param request:
    :param idRol:
    :return:
    """
    mensaje="Usuario eliminido con exito"
    usuario = User.objects.get(pk=idUsuario)
    usuario.delete()
    usuario_actor = request.user
    lista_usuarios = User.objects.all()
    return render_to_response('usuario/operacion_usuario_exito.html', {'mensaje':mensaje, 'usuario_actor': usuario_actor, 'lista_usuarios': lista_usuarios}, context_instance=RequestContext(request))



@login_required(login_url = '/')
def cerrar_sesion(request):
    """
    Vista para cerrar la sesion de un ususario

    Recibe como parametro un request y llama a la funcion logout con tal parametro, redirigiendo al
    usuario a la pagina web '/' (raiz) donde se solicita el inicio de sesion de un usuario
    """
    logout(request)
    return HttpResponseRedirect('/')

