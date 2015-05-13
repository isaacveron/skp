from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from apps.usuario.models import User
from apps.sprint.models import Sprint
from apps.proyectos.models import Proyecto
from apps.sprint.forms import SprintForm, SprintFormMod, SprintFormDelete
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.decorators import user_passes_test
from django.db.models import Q
from apps.userstory.models import UserStory

# Create your views here.
@login_required(login_url = '/')
def gestion_de_sprint(request):
  """
    Recibe un request, obtiene la lista de todos los sprints del sistema y 
    luego retorna el html renderizado con la lista de sprints 

    @type request: django.http.HttpRequest
    @param request: Contiene informacion sobre la solic. web actual que llamo a esta vista
    @rtype: django.http.HttpResponse
    @return: gestion_de_proyectos.html, donde se listan los proyectos
    @author: Isaac Veron 
  """
  usuario_actor = request.user
  sprints = Sprint.objects.all()
  return render_to_response('sprint/gestion_de_sprint.html',
                              {'usuario_actor': usuario_actor, 'sprints': sprints}, context_instance=RequestContext(request))


@login_required(login_url = '/')
@user_passes_test( User.can_add_proyecto , login_url="/index/")
def crear_sprint(request, idProyecto):
    """
     Vista de creacion de nuevo Sprint 
    Recibe como parametro un request y retorna la pagina web crear_sprint.html donde se debe completar
    los datos del Sprint y luego operacion_sprint_exito.html si se completo debidamente el formulario
    * Variables
        -usuario_actor: es el usuario que realiza la accion
        -formulario: es el fomrulario que debe completar el usuario_actor
    @type request: django.http.HttpRequest
    @param request: Contiene informacion sobre la solic. web actual que llamo a esta vista  
    @rtype: django.http.HttpResponse
    @return: operacion_sprint_exito.html, mensaje de exito
    @author: Isaac Veron
    """
    proyecto = Proyecto.objects.get(pk=idProyecto)
    mensaje="Sprint creado con exito"
    usuario_actor = request.user
    sprint = Sprint( Usuario_creador=usuario_actor, Proyecto_asignado=proyecto)
    

    if request.method == 'POST':
        formulario = SprintFormMod(request.POST, instance=sprint)
        if formulario.is_valid():

            sprint = formulario.save()

            for us in sprint.UserStorys.all():
                sprint.Duracion += us.Duracion

            cambiar_estado_userstory("asignar",formulario.instance.pk)

            userstorys = UserStory.objects.filter( Proyecto_asignado=proyecto )

            for us in userstorys:

                if( us.in_kanban ):

                    us.in_kanban = False
                    actividad = us.Actividad_asignada
                    us.Estado_de_actividad = 'none'
                    us.Estado = 'AsignadoSprint'

                    actividad.To_do.remove(us)
                    actividad.Doing.remove(us)
                    actividad.Done.remove(us)
                    actividad.save()
                    us.save()

                    sprint.UserStorys.add(us)

            sprint.save()
            return render_to_response('sprint/operacion_sprint_exito.html',
                                      {'mensaje': mensaje, 'usuario_actor': usuario_actor, 'proyecto':proyecto},
                                      context_instance=RequestContext(request))
    else:
        formulario = SprintForm(idProyecto=idProyecto)

    return render_to_response('sprint/crear_sprint.html',
                              {'formulario': formulario, 'operacion': 'Crear Sprint',
                               'usuario_actor': usuario_actor, 'proyecto':proyecto},
                              context_instance=RequestContext(request))

def detalle_sprint(request, idSprint):
    """ 
      Busca en la base de datos al sprint cuyos datos se quieren consultar y los presenta en un vista html
    
      @type request: django.http.HttpRequest
      @param request: Contiene informacion sobre la solic. web actual que llamo a esta vista
      @type idSprint: integer
      @param idSprint: es el id del sprint cuyos datos se quieren consultar
      @rtype: django.HttpResponse
      @return: detalle_sprint.html, donde se le despliega al usuario los datos
      @author: Isaac Veron
    """
    
    usuario_actor = request.user
    sprint = Sprint.objects.get(pk=idSprint)

    return render_to_response('sprint/detalle_sprint.html', {'usuario_actor': usuario_actor, 'sprint':sprint},
                              context_instance=RequestContext(request))

@login_required(login_url = '/')
def buscar_sprint(request):
    """
    Vista para buscar un sprint dentro del listado de sprints del sistema

    @return: Se retorna a la pagina de vista con el sprint que coincida con el query o vacio
    @author: Isaac Veron
    """
    usuario_actor = request.user
    query = request.GET.get('q', '')
    if query:
        qset = (
            Q(Nombre=query)
        )
        results = Sprint.objects.filter(qset).distinct()
    else:
        results = []
    return render_to_response('sprint/gestion_de_sprint.html', {'usuario_actor': usuario_actor, 'sprints': results}, context_instance=RequestContext(request))


@login_required(login_url = '/')
@user_passes_test( User.can_change_proyecto , login_url="/index/")
def modificar_sprint(request, idSprint):
    """
    Busca en la base de datos el sprint cuyos datos se quieren modificar.
    Presenta esos datos en un formulario y luego se guardan los cambios realizados.
     
    @type request: django.http.HttpRequest
    @param request: Contiene informacion sobre la solic. web actual que llamo a esta vista
    @type idSprint: integer
    @param idSprint: es el id del spirnt cuyos datos se quieren modificar
    @rtype: django.HttpResponse
    @return: modificar_sprint.html,un formulario donde se despliegan los datos que el usuario puede modificar,
    una vez modificado renderiza a la pagina de exito
    @author: Isaac Veron
    """
    mensaje="Sprint modificado correctamente"
    usuario_actor = request.user
    sprint = Sprint.objects.get(pk=idSprint)
    formulario = SprintFormMod(request.POST,instance=sprint)
    if formulario.is_valid():
        if 'Confirmar' in request.POST:
            formulario.save()
            cambiar_estado_userstory("asignar",idSprint)
            return render_to_response('sprint/operacion_sprint_exito.html',{'mensaje':mensaje}, context_instance=RequestContext(request))
        elif 'Cancelar' in request.POST:
            cambiar_estado_userstory("asignar",idSprint)
            return HttpResponseRedirect('/index/')
    else:
        formulario = SprintFormMod(instance=sprint)
        cambiar_estado_userstory("desasignar",idSprint)
    return render_to_response('sprint/modificar_sprint.html',{'usuario_actor': usuario_actor, 'sprint':sprint, 'formulario':formulario},context_instance=RequestContext(request))


@login_required(login_url = '/')
def cambiar_estado_sprint(request, idSprint):

    """
    Cambia el estado de activo a no activo


    @type idSprint: integer
    @param idSprint: es el id del spirnt cuyos datos se quieren modificar
    @rtype: django.HttpResponse
    @return:cambiar_estado_sprint.html,un formulario donde se despliegan los datos que el usuario puede modificar
    una vez modificado renderiza a la pagina de exito
    @author: Isaac Veron
    """

    mensaje = "Cambio de estado de Sprint con exito"
    sprint = Sprint.objects.get(pk=idSprint)
    if request.method == 'POST':
        formulario = SprintFormDelete(request.POST, instance=sprint)
        if formulario.is_valid():
           formulario.save()
           cambiar_estado_userstory("desasignar",idSprint)

           return render_to_response('sprint/operacion_sprint_exito.html',{'mensaje': mensaje}, context_instance=RequestContext(request))
    else:
        formulario = SprintFormDelete(instance=sprint)
    return render_to_response('sprint/cambiar_estado_sprint.html',{'formulario': formulario},context_instance=RequestContext(request))

@login_required(login_url = '/')
@user_passes_test( User.can_delete_proyecto , login_url="/index/")
def vista_eliminar_sprint(request, idSprint):
    """
    Esta vista obtiene el sprint que quiere ser eliminado, pregunta si quiere ser eliminado y llama 
    a la funcion eliminar_sprint

    @param request: django.http.HttpRequest
    @param idProyecto: Contiene el identificador del sprint a ser eliminado
    @return: se retorna la pagina de eliminacion de sprint
    @author: Isaac Veron
    """
    usuario_actor = request.user
    sprint = Sprint.objects.get(pk=idSprint)
    return render_to_response('sprint/eliminar_sprint.html', {'usuario_actor': usuario_actor, 'sprint': sprint}, context_instance=RequestContext(request))


@login_required(login_url = '/')
def eliminar_sprint(request, idSprint):
    """
    Eliminar de manera fisica los registros del sprint

    @type request: django.http.HttpRequest
    @param request: Contiene informacion sobre la solicitud web actual que llamo a esta vista  
    @type idSprint: integer
    @param idSprint: Contiene el id del sprint a ser eliminado.
    @rtype: django.shortcuts.render_to_response
    @return: Se retorna a la a la pagina de notificacion de exito
    @author: Isaac Veron
    """

    mensaje = "Sprint eliminado con exito"
    sprint = Sprint.objects.get(pk=idSprint)

    for us in sprint.UserStorys.all():
        us.Estado = 'Pendiente'
        us.save()

    sprint.delete()
    usuario_actor = request.user
    return render_to_response('sprint/operacion_sprint_exito.html',{'mensaje':mensaje, 'usuario_actor': usuario_actor}, context_instance=RequestContext(request))


def cambiar_estado_userstory(accion, idSprint):
    """
    Esta funcion cambia el esdado de los us de un sprint
    Ya sea a Pendiente o AsignadoSprint
    """
    if accion=="asignar":
        sprint = Sprint.objects.get(pk=idSprint)
        for us in sprint.UserStorys.all():
            us.Estado="AsignadoSprint"
            us.save()
    elif accion=="desasignar":
        sprint = Sprint.objects.get(pk=idSprint)
        for us in sprint.UserStorys.all():
            us.Estado="Pendiente"
            us.save()




##############################################################################################################################

def vista_iniciar_sprint(request, idSprint):

    """
        Vista que despliega la pagina de confirmacion para el inicio de sprints

        @type request: django.http.HttpRequest
        @param request: Contiene informacion sobre la solicitud web actual que llamo a esta vista
        @type idSprint : integer
        @param idSprint : Contiene el id del Sprint que se desea iniciar.
        @rtype: django.shortcuts.render_to_response
        @return: retorn un HttpResponse a la pagina de inicio de sprint
        @author: Cesar Recalde
    """

    sprint = Sprint.objects.get(pk=idSprint)
    usuario_actor = request.user

    return render_to_response('sprint/iniciar_sprint.html',{'sprint':sprint, 'usuario_actor': usuario_actor},
                            context_instance=RequestContext(request))



def iniciar_sprint(request, idSprint):
    """
        Vista que cambia el estado del sprint de 'Pendiente' a 'En_curso', o sea, lo inicia,
        realizando en el proceso todos los cambios necesarios en los user storys y las tablas kanban

        @type request: django.http.HttpRequest
        @param request: Contiene informacion sobre la solicitud web actual que llamo a esta vista
        @type idSprint : integer
        @param idSprint : Contiene el id del Sprint que se desea iniciar.
        @rtype: django.shortcuts.render_to_response
        @return: retorn un HttpResponse a la pagina de notificacioin de exito
        @author: Cesar Recalde
    """

    usuario_actor = request.user
    mensaje = 'Sprint iniciado'

    sprint = Sprint.objects.get(pk=idSprint)
    tabla = sprint.Tabla_asignada
    actividad = tabla.Actividades.get(Orden = 1)

    for us in sprint.UserStorys.all():

        us.in_kanban = True
        us.Estado_de_actividad = 'to_do'
        us.Actividad_asignada = actividad
        actividad.To_do.add(us)

        us.Estado = 'AsignadoSprintActivo'
        us.save()

    actividad.save()
    tabla.save()

    sprint.Estado = 'En_curso'
    sprint.save()

    return render_to_response('sprint/operacion_sprint_exito.html',{'mensaje':mensaje, 'usuario_actor': usuario_actor},
                            context_instance=RequestContext(request))

def vista_detener_sprint(request, idSprint):

    """
        Vista que despliega la pagina de confirmacion para la detencion de sprints

        @type request: django.http.HttpRequest
        @param request: Contiene informacion sobre la solicitud web actual que llamo a esta vista
        @type idSprint : integer
        @param idSprint : Contiene el id del Sprint que se desea detener.
        @rtype: django.shortcuts.render_to_response
        @return: retorn un HttpResponse a la pagina de detencion de sprint
        @author: Cesar Recalde
    """

    sprint = Sprint.objects.get(pk=idSprint)
    usuario_actor = request.user

    return render_to_response('sprint/detener_sprint.html',{'sprint':sprint, 'usuario_actor': usuario_actor},
                            context_instance=RequestContext(request))

def detener_sprint(request, idSprint):
    """
        Vista que cambia el estado del sprint de 'En_curso' a 'Pendiente', o sea, lo detiene,
        realizando en el proceso todos los cambios necesarios en los user storys y las tablas kanban

        @type request: django.http.HttpRequest
        @param request: Contiene informacion sobre la solicitud web actual que llamo a esta vista
        @type idSprint : integer
        @param idSprint : Contiene el id del Sprint que se desea detener.
        @rtype: django.shortcuts.render_to_response
        @return: retorn un HttpResponse a la pagina de notificacioin de exito
        @author: Cesar Recalde
    """
    usuario_actor = request.user
    mensaje = 'Sprint detenido'

    sprint = Sprint.objects.get(pk=idSprint)
    tabla = sprint.Tabla_asignada



    for us in sprint.UserStorys.all():

        actividad = us.Actividad_asignada
        actividad.To_do.remove(us)
        actividad.Doing.remove(us)
        actividad.Done.remove(us)

        us.Estado = 'AsignadoSprint'
        us.in_kanban = False
        us.Estado_de_actividad = 'none'

        us.save()
        actividad.save()


    tabla.save()

    sprint.Estado = 'Pendiente'
    sprint.save()

    return render_to_response('sprint/operacion_sprint_exito.html',{'mensaje':mensaje, 'usuario_actor': usuario_actor}, 
                            context_instance=RequestContext(request))