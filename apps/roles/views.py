from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from apps.roles.forms import RolForm, AsignarRol
from django.contrib.auth.models import User, Group, Permission
from django.contrib.auth.decorators import login_required, permission_required
from django.db.models import Q


# Create your views here.

@login_required(login_url = '/')
@permission_required('auth.add_group', login_url='/index/')
def crear_rol(request):
    """
    Vista de creacion de nuevo rol
    Recibe como parametro un request y retorna la pagina web crear_rol.html donde se debe completar
    los datos del rol y luego crear_rol_exito.html si se completo debidamente el formulario
    * Variables
        -usuario_actor: es el usuario que realiza la accion
        -formulario: es el fomrulario que debe completar el usuario_actor
        -roles: es la lista de roles existentes en el sistema
    @type request: django.http.HttpRequest
    @param request: Contiene informacion sobre la solic. web actual que llamo a esta vista  
    @rtype: django.http.HttpResponse
    @return: rolcreado.html, mensaje de exito
    @author: Isaac Veron
    """

    mensaje="Rol creado con exito"
    usuario_actor = request.user
    rol = Group(Usuario=usuario_actor)
    if request.method == 'POST':
        formulario = RolForm(request.POST, instance=rol)
        if formulario.is_valid():
            formulario.save()
            roles = Group.objects.all()
            return render_to_response('rol/operacion_rol_exito.html',
                                      {'mensaje': mensaje, 'usuario_actor': usuario_actor, 'roles': roles},
                                      context_instance=RequestContext(request))
    else:
        formulario = RolForm()
    return render_to_response('rol/crear_rol.html',
                              {'formulario': formulario, 'operacion': 'Crear rol',
                               'usuario_actor': usuario_actor},
                              context_instance=RequestContext(request))


@login_required(login_url = '/')
def administrar_roles(request):
    """
    Recibe un request, obtiene la lista de todos los Roles del sistema y 
    luego retorna el html renderizado con la lista de roles

    @type request: django.http.HttpRequest
    @param request: Contiene informacion sobre la solic. web actual que llamo a esta vista
    @rtype: django.http.HttpResponse
    @return: administrar_rol.html, donde se listan los Roles    
    @author: Isaac Veron
    """

    usuario_actor = request.user
    roles = Group.objects.all()
    return render_to_response('rol/administrar_rol.html',
                              {'usuario_actor': usuario_actor, 'roles': roles}, context_instance=RequestContext(request))


@login_required(login_url = '/')
def detalle_rol(request, idRol):
    """ 
    Busca en la base de datos al Rol cuyos datos se quieren consultar y los presenta en un vista html
    
    @type request: django.http.HttpRequest
    @param request: Contiene informacion sobre la solic. web actual que llamo a esta vista
    @type idRol: integer
    @param idRol: es el id del Rol cuyos datos se quieren consultar
    @rtype: django.HttpResponse
    @return: detalle_rol.html, donde se le despliega al usuario los datos
    @author: Isaac Veron
    """

    usuario_actor = request.user
    rol = Group.objects.get(pk=idRol)
    return render_to_response('rol/detalle_rol.html', {'usuario_actor': usuario_actor, 'rol': rol},
                              context_instance=RequestContext(request))



@login_required(login_url = '/')
@permission_required('auth.change_group', login_url='/index/')
def modificar_rol(request, idRol):
    """
    Busca en la base de datos el Rol cuyos datos se quieren modificar.
    Presenta esos datos en un formulario y luego se guardan los cambios realizados.
     
    @type request: django.http.HttpRequest
    @param request: Contiene informacion sobre la solic. web actual que llamo a esta vista
    @type idRol: integer
    @param idRol: es el id del rol cuyos datos se quieren modificar
    @rtype: django.HttpResponse
    @return: modificar_rol.html,un formulario donde se despliegan los datos que el usuario puede modificar,
    una vez modificado renderiza a la pagina donde se listan todos los roles 
    @author: Isaac Veron
    """

    usuario_actor = request.user
    rol = Group.objects.get(pk=idRol)
    formulario = RolForm(request.POST, instance=rol)
    if formulario.is_valid():
        formulario.save()
        return HttpResponseRedirect('/listar_roles/')
    else:
        formulario = RolForm(instance=rol)
    return render_to_response('rol/modificar_rol.html',
                              {'usuario_actor': usuario_actor, 'rol':rol, 'formulario':formulario},
                              context_instance=RequestContext(request))


@login_required(login_url = '/')
@permission_required('auth.delete_group', login_url='/index/')
def vista_eliminar_rol(request, idRol):
    """
    Esta vista obtiene el rol que quiere ser eliminado, pregunta si quiere ser eliminado y llama 
    a la funcion eliminar_usuario

    :param request:
    :param idRol:
    :return:
    """
    usuario_actor = request.user
    rol = Group.objects.get(pk=idRol)
    return render_to_response('rol/eliminar_rol.html', {'usuario_actor': usuario_actor, 'rol': rol},
                              context_instance=RequestContext(request))


@login_required(login_url = '/')
@permission_required('auth.delete_group', login_url='/index/')
def eliminar_rol(request, idRol):
    """
    Eliminar de manera logica los registros del rol.
        
    @type request: django.http.HttpRequest
    @param request: Contiene informacion sobre la solicitud web actual que llamo a esta vista  
    @type idRol : integer
    @param idRol : Contiene el id del rol a ser eliminado.
    @rtype: django.shortcuts.render_to_response
    @return: Se retorna a la a la pagina de notificacion de exito
    @author: Isaac Veron
    """

    mensaje = "Rol eliminado con exito"
    rol = Group.objects.get(pk=idRol)
    rol.delete()
    usuario_actor = request.user
    roles = Group.objects.all()
    return render_to_response('rol/operacion_rol_exito.html',
                              {'mensaje':mensaje, 'usuario_actor': usuario_actor, 'roles': roles},
                              context_instance=RequestContext(request))


@login_required(login_url = '/')
def buscar_rol(request):
    """
    Vista para buscar un usuario dentro del listado de usuarios del sistema

    @return: Se retorna a la a la pagina de vista de roles con el rol que coinciden con el query o vacio
    @author: Isaac Veron
    """

    query = request.GET.get('q', '')
    if query:
        qset = (
            Q(name=query)
        )
        results = Group.objects.filter(qset).distinct()
    else:
        results = []
    return render_to_response('rol/administrar_rol.html', {'roles': results}, context_instance=RequestContext(request))

