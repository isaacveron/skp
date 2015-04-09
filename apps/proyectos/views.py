from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from apps.proyectos.forms import ProyectoForm
from apps.roles.models import Group
from apps.usuario.models import User
from apps.proyectos.models import Proyecto
from django.contrib.auth.decorators import login_required, permission_required

# Create your views here.
@login_required(login_url = '/')
def gestion_de_proyectos(request):
    usuario_actor = request.user
    proyectos = Proyecto.objects.all()
    return render_to_response('proyecto/gestion_de_proyectos.html',
                              {'usuario_actor': usuario_actor, 'proyectos': proyectos}, context_instance=RequestContext(request))


@login_required(login_url = '/')
def crear_proyecto(request):
    """
    Vista de creacion de nuevo Proyecto

    Recibe como parametro un request y retorna la pagina web crear_rol.html donde se debe completar
    los datos del rol y luego crear_rol_exito.html si se completo debidamente el formulario
    * Variables
        -   usuario_actor: es el usuario que realiza la accion
        -   formulario: es el fomrulario que debe completar el usuario_actor
        -   roles: es la lista de roles existentes en el sistema
    """
    mensaje="Proyecto creado con exito"
    usuario_actor = request.user
    rol = Group(Usuario=usuario_actor)
    if request.method == 'POST':
        formulario = ProyectoForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            Usuarios = User.objects.all()
            return render_to_response('proyecto/operacion_proyecto_exito.html',
                                      {'mensaje': mensaje, 'usuario_actor': usuario_actor, 'usuarios': Usuarios},
                                      context_instance=RequestContext(request))
    else:
        formulario = ProyectoForm()
    return render_to_response('proyecto/crear_proyecto.html',
                              {'formulario': formulario, 'operacion': 'Crear Proyecto',
                               'usuario_actor': usuario_actor},
                              context_instance=RequestContext(request))


def detalle_proyecto(request, idProyecto):
    usuario_actor = request.user
    proyecto = Proyecto.objects.get(pk=idProyecto)
    return render_to_response('proyecto/detalle_proyecto.html', {'usuario_actor': usuario_actor, 'proyecto': proyecto},
                              context_instance=RequestContext(request))