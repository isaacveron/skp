from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, authenticate
from django.contrib.auth import	login, authenticate, logout 
from apps.usuario.forms import UsuarioForm, UsuarioModForm
from apps.roles.forms import AsignarRol
from apps.proyectos.models import Proyecto
from apps.userstory.models import UserStory
from django.contrib.auth.models import User, Group, Permission
from django.contrib.auth.decorators import login_required, permission_required
from django.views.decorators.csrf import csrf_protect
from django.db.models import Q

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
    @type request: django.http.HttpRequest
    @param request: Contiene informacion sobre la solicitud web actual que llamo a esta vista
    @rtype: django.http.HttpResponseRedirect
    @rtype: django.shortcuts.render_to_response
    @return: Se retorna al inicio o se manda a la pagina de login
    @author: Isaac Veron  
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
    """
    Vista principal del sistema
    @rtype: django.http.HttpResponseRedirect
    @author: Isaac Veron
    """
    usuario_actor = request.user
    proyectos = Proyecto.objects.all()
    return render_to_response('index.html', {'usuario_actor':usuario_actor, 'proyectos':proyectos}, context_instance = RequestContext(request))


@login_required(login_url = '/')
@permission_required('auth.add_user', login_url='/index/')
def crear_usuario(request):
    """
    Vista de creacion de nuevo usuario

    Recibe como parametro un request y retorna la pagina web form_usuario.html donde se debe completar
    los datos del usuario y luego operacion_usuario_exito.html si se completo debidamente el formulario
    * Variables
        -   usuario_actor: es el usuario que realiza la accion
        -   formulario: es el fomrulario que debe completar el usuario_actor
        -   lista_usuarios: es la lista de usuarios existentes en el sistema
    @type request: django.http.HttpRequest
    @param request: Contiene informacion sobre la solic. web actual que llamo a esta vista
    @rtype: django.http.HttpResponse
    @return: usuariocreado.html, mensaje de exito
    @author: Isaac Veron
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


@login_required(login_url = '/')
def administrar_usuario(request):
    """
    Vista de administrar usuario

    Recibe como parametro un request y retorna la pagina web administrar_usuario.html donde se muestra
    la lista de usuarios si el usuario_actor posee los permsos correspondientes

    * Variables
        -   usuario_actor: es el usuario que realiza la accion
        -   lista_usuarios: es la lista de usuarios existentes en el sistema
    
    @type request: django.http.HttpRequest
    @param request: Contiene informacion sobre la solic. web actual que llamo a esta vista
    @rtype: django.http.HttpResponse
    @return: usuarios.html, donde se listan los usuarios, ademas de las funcionalidades para un usuario
    @author: Isaac Veron
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

    @type request: django.http.HttpRequest
    @param request: Contiene informacion sobre la solic. web actual que llamo a esta vista
    @type idUsuario: integer
    @param idUsuario: es el id del usuario cuyos datos se quieren consultar
    @rtype: django.HttpResponse
    @return: detalle_usuario.html, donde se le despliega al usuario los datos
    @author: Isaac Veron
    """

    usuario_parametro = User.objects.get(pk=idUsuario)
    return render_to_response('usuario/detalle_usuario.html', {'usuario_actor': request.user,'usuario_parametro': usuario_parametro}, context_instance=RequestContext(request))


@login_required(login_url = '/')
@permission_required('auth.change_user', login_url='/index/')
def modificar_usuario(request, idUsuario):
    """"  
    Vista de modificacion de nuevo usuario

    Recibe como parametro un request y retorna la pagina web form_usuario.html donde se debe completar
    los datos el usuario y luego operacion_usuario_exito.html si se completo debidamente el formulario
    * Variables
        -   usuario_actor: es el usuario que realiza la accion
        -   formulario: es el fomrulario que debe completar el usuario_actor
        -   lista_usuarios: es la lista de usuarios existentes en el sistema

    @type request: django.http.HttpRequest
    @param request: Contiene informacion sobre la solic. web actual que llamo a esta vista
    @type idUsuario: integer
    @param idUsuario: es el id del usuario cuyos datos se quieren modificar
    @rtype: django.HttpResponse
    @return: modificar_usuario.html,un formulario donde se despliegan los datos que el usuario puede modificar,
    operacion_usuario_exito.html, donde se notifica al usuario el exito de la operacion 
    @author: Isaac Veron
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


@login_required(login_url = '/')
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


@login_required(login_url = '/')
def vista_eliminar_usuario(request, idUsuario):
    """ 
    Esta vista obtiene el usuario que quiere ser eliminado, pregunta si quiere ser eliminado y llama 
    a la funcion eliminar_usuario

    :param request:
    :param idRol:
    :return:
    """
    usuario_actor = request.user
    usuario_parametro = User.objects.get(pk=idUsuario)
    return render_to_response('usuario/eliminar_usuario.html', {'usuario_actor': usuario_actor, 'usuario_parametro': usuario_parametro},
                              context_instance=RequestContext(request))


@login_required(login_url = '/')
@permission_required('auth.delete_user', login_url='/index/')
def eliminar_usuario(request, idUsuario):
    """
    Recibe el id del usuario que se desea eliminar y lo elimina de la base de datos

    @type request: django.http.HttpRequest
    @param request: Contiene informacion sobre la solicitud web actual que llamo a esta vista
    @type idUsuario : integer
    @param idUsuario : Contiene el id del usuario a ser eliminado.
    @rtype: django.shortcuts.render_to_response
    @return: retorna a la pagina de eliminacion exitosa
    @author: Isaac Veron
    """

    mensaje="Usuario eliminido con exito"
    usuario = User.objects.get(pk=idUsuario)
    usuario.delete()
    usuario_actor = request.user
    lista_usuarios = User.objects.all()
    return render_to_response('usuario/operacion_usuario_exito.html', {'mensaje':mensaje, 'usuario_actor': usuario_actor, 'lista_usuarios': lista_usuarios}, context_instance=RequestContext(request))


@login_required(login_url = '/')
def buscar_usuario(request):
    """
    Vista para buscar un usuario dentro del listado de usuarios del sistema

    @return: Se retorna a la a la pagina de vista de usuario(s) con los roles que coinciden con el query o vacio
    @author: Isaac Veron
    """

    query = request.GET.get('q', '')
    if query:
        qset = (
            Q(username=query) |
            Q(first_name=query) |
            Q(last_name=query)
        )
        results = User.objects.filter(qset).distinct().order_by('is_active').reverse()
    else:
        results = []
    return render_to_response('usuario/administrar_usuario.html', {'lista_usuarios': results}, context_instance=RequestContext(request))


@login_required(login_url = '/')
def cerrar_sesion(request):
    """
    Vista para cerrar la sesion de un ususario.
    Recibe como parametro un request y llama a la funcion logout con tal parametro, redirigiendo al
    usuario a la pagina web '/' (raiz) donde se solicita el inicio de sesion de un usuario
    """
    logout(request)
    return HttpResponseRedirect('/')

