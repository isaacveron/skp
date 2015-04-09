from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from apps.roles.forms import RolForm, AsignarRol
from django.contrib.auth.models import User, Group, Permission
from django.contrib.auth.decorators import login_required, permission_required

# Create your views here.



@login_required(login_url = '/')
def crear_rol(request):
    """
    Vista de creacion de nuevo rol

    Recibe como parametro un request y retorna la pagina web crear_rol.html donde se debe completar
    los datos del rol y luego crear_rol_exito.html si se completo debidamente el formulario
    * Variables
        -   usuario_actor: es el usuario que realiza la accion
        -   formulario: es el fomrulario que debe completar el usuario_actor
        -   roles: es la lista de roles existentes en el sistema
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

def administrar_roles(request):
    usuario_actor = request.user
    roles = Group.objects.all()
    return render_to_response('rol/administrar_rol.html',
                              {'usuario_actor': usuario_actor, 'roles': roles}, context_instance=RequestContext(request))

def detalle_rol(request, idRol):
    usuario_actor = request.user
    rol = Group.objects.get(pk=idRol)
    return render_to_response('rol/detalle_rol.html', {'usuario_actor': usuario_actor, 'rol': rol},
                              context_instance=RequestContext(request))

def modificar_rol(request, idRol):
    """

    :param request:
    :param idRol:
    :return:
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

def vista_eliminar_rol(request, idRol):
    """

    :param request:
    :param idRol:
    :return:
    """
    usuario_actor = request.user
    rol = Group.objects.get(pk=idRol)
    return render_to_response('rol/eliminar_rol.html', {'usuario_actor': usuario_actor, 'rol': rol},
                              context_instance=RequestContext(request))

def eliminar_rol(request, idRol):
    """

    :param request:
    :param idRol:
    :return:
    """
    mensaje = "Rol eliminado con exito"
    rol = Group.objects.get(pk=idRol)
    rol.delete()
    usuario_actor = request.user
    roles = Group.objects.all()
    return render_to_response('rol/operacion_rol_exito.html',
                              {'mensaje':mensaje, 'usuario_actor': usuario_actor, 'roles': roles},
                              context_instance=RequestContext(request))

