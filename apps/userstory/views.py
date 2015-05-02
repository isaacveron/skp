from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from apps.usuario.models import User
from apps.proyectos.models import Proyecto
from apps.userstory.models import UserStory
from apps.flujos.models import Flujo, Actividad
from apps.sprint.models import Sprint
from apps.userstory.forms import UserStoryForm, UserStoryFormDelete, UserStoryFormMod
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.decorators import user_passes_test
from django.db.models import Q

# Create your views here.
@login_required(login_url = '/')
def gestion_de_userstory(request):
  """
    Recibe un request, obtiene la lista de todos los proyectos del sistema y 
    luego retorna el html renderizado con la lista de proyectos 

    @type request: django.http.HttpRequest
    @param request: Contiene informacion sobre la solic. web actual que llamo a esta vista
    @rtype: django.http.HttpResponse
    @return: gestion_de_proyectos.html, donde se listan los proyectos
    @author: Cesar Recalde
  """
  usuario_actor = request.user
  userstorys = UserStory.objects.all()
  return render_to_response('userstory/gestion_de_userstory.html',
                              {'usuario_actor': usuario_actor, 'userstorys': userstorys}, context_instance=RequestContext(request))


@login_required(login_url = '/')
@user_passes_test( User.can_add_proyecto , login_url="/index/")
def crear_userstory(request, idProyecto):
    """
     Vista de creacion de nuevo Proyecto
    Recibe como parametro un request y retorna la pagina web crear_Proyecto.html donde se debe completar
    los datos del Proyecto y luego operacion_proyecto_exito.html si se completo debidamente el formulario
    * Variables
        -usuario_actor: es el usuario que realiza la accion
        -formulario: es el fomrulario que debe completar el usuario_actor
        -proyectos: es la lista de proyectos existentes en el sistema
    @type request: django.http.HttpRequest
    @param request: Contiene informacion sobre la solic. web actual que llamo a esta vista  
    @rtype: django.http.HttpResponse
    @return: operacion_proyecto_exito.html, mensaje de exito
    @author: Cesar Recalde
    """
    proyecto = Proyecto.objects.get(pk=idProyecto)
    mensaje="User Story creado con exito"
    usuario_actor = request.user
    userstory = UserStory( Usuario_creador=usuario_actor, Proyecto_asignado=proyecto)
    if request.method == 'POST':
        formulario = UserStoryFormMod(request.POST, instance=userstory)
        if formulario.is_valid():
            formulario.save()
            userstorys = UserStory.objects.all()
            return render_to_response('userstory/operacion_userstory_exito.html',
                                      {'mensaje': mensaje, 'usuario_actor': usuario_actor, 'userstorys': userstorys, 'proyecto':proyecto},
                                      context_instance=RequestContext(request))
    else:
        formulario = UserStoryForm(idProyecto)
    return render_to_response('userstory/crear_userstory.html',
                              {'formulario': formulario, 'operacion': 'Crear User Story',
                               'usuario_actor': usuario_actor, 'proyecto':proyecto},
                              context_instance=RequestContext(request))

def detalle_userstory(request, idUserStory):
    """ 
      Busca en la base de datos al proyecto cuyos datos se quieren consultar y los presenta en un vista html
    
      @type request: django.http.HttpRequest
      @param request: Contiene informacion sobre la solic. web actual que llamo a esta vista
      @type idProyecto: integer
      @param idProyecto: es el id del proyecto cuyos datos se quieren consultar
      @rtype: django.HttpResponse
      @return: detalle_proyecto.html, donde se le despliega al usuario los datos
      @author: Cesar Recalde
    """
   
    usuario_actor = request.user
    userstory = UserStory.objects.get(pk=idUserStory)
    tabla = Flujo.objects.get( pk = userstory.Actividad_asignada.idTabla )

    return render_to_response('userstory/detalle_userstory.html', {'usuario_actor': usuario_actor, 'userstory': userstory, 'tabla':tabla},
                              context_instance=RequestContext(request))

@login_required(login_url = '/')
def buscar_userstory(request):
    """
    Vista para buscar un proyecto dentro del listado de proyectos del sistema

    @return: Se retorna a la pagina de vista de proyectos con el proyecto que coincida con el query o vacio
    @author: Cesar Recalde
    """
    usuario_actor = request.user
    query = request.GET.get('q', '')
    if query:
        qset = (
            Q(Nombre=query)
        )
        results = UserStory.objects.filter(qset).distinct()
    else:
        results = []
    return render_to_response('userstory/gestion_de_userstory.html', {'usuario_actor': usuario_actor, 'userstorys': results}, context_instance=RequestContext(request))


@login_required(login_url = '/')
@user_passes_test( User.can_change_proyecto , login_url="/index/")
def modificar_userstory(request, idUserStory):
    """
    Busca en la base de datos el Proyecto cuyos datos se quieren modificar.
    Presenta esos datos en un formulario y luego se guardan los cambios realizados.
     
    @type request: django.http.HttpRequest
    @param request: Contiene informacion sobre la solic. web actual que llamo a esta vista
    @type idProyecto: integer
    @param idProyecto: es el id del Proyecto cuyos datos se quieren modificar
    @rtype: django.HttpResponse
    @return: modificar_Proyecto.html,un formulario donde se despliegan los datos que el usuario puede modificar,
    una vez modificado renderiza a la pagina donde se listan todos los proyectos
    @author: Cesar Recalde
    """

    usuario_actor = request.user
    userstory = UserStory.objects.get(pk=idUserStory)
    formulario = UserStoryFormMod(request.POST, instance=userstory)
    if formulario.is_valid():
        formulario.save()
        return HttpResponseRedirect('/gestion_de_userstory/')
    else:
        formulario = UserStoryFormMod(instance=userstory)
    return render_to_response('userstory/modificar_userstory.html',
                              {'usuario_actor': usuario_actor, 'userstory':userstory, 'formulario':formulario},
                              context_instance=RequestContext(request))

@login_required(login_url = '/')
def cambiar_estado_userstory(request, idUserStory):
    mensaje = "Cambio de estado de UserStory con exito"
    userstory = UserStory.objects.get(pk=idUserStory)
    if request.method == 'POST':
        formulario = UserStoryFormDelete(request.POST, instance=userstory)
        if formulario.is_valid():
           formulario.save()
           return render_to_response('userstory/operacion_userstory_exito.html',{'mensaje': mensaje}, context_instance=RequestContext(request))
    else:
        formulario = UserStoryFormDelete(instance=userstory)
    return render_to_response('userstory/cambiar_estado_userstory.html',{'formulario': formulario},context_instance=RequestContext(request))



@login_required(login_url = '/')
@user_passes_test( User.can_delete_proyecto , login_url="/index/")
def vista_eliminar_userstory(request, idUserStory):
    """
    Esta vista obtiene el proyecto que quiere ser eliminado, pregunta si quiere ser eliminado y llama 
    a la funcion eliminar_proyecto

    @param request: django.http.HttpRequest
    @param idProyecto: Contiene el identificador del proyecto a ser eliminado
    @return: se retorna la pagina de eliminacion de proyectos
    @author: Cesar Recalde
    """
    usuario_actor = request.user
    userstory = UserStory.objects.get(pk=idUserStory)
    return render_to_response('userstory/eliminar_userstory.html', {'usuario_actor': usuario_actor, 'userstory': userstory},
                              context_instance=RequestContext(request))


@login_required(login_url = '/')
def eliminar_userstory(request, idUserStory):
    """
    Eliminar de manera logica los registros del proyecto.
        
    @type request: django.http.HttpRequest
    @param request: Contiene informacion sobre la solicitud web actual que llamo a esta vista  
    @type idProyecto : integer
    @param idProyecto : Contiene el id del proyecto a ser eliminado.
    @rtype: django.shortcuts.render_to_response
    @return: Se retorna a la a la pagina de notificacion de exito
    @author: Cesar Recalde
    """

    mensaje = "UserStory eliminado con exito"
    userstory = UserStory.objects.get(pk=idUserStory)
    userstory.delete()
    usuario_actor = request.user
    return render_to_response('userstory/operacion_userstory_exito.html',
                              {'mensaje':mensaje, 'usuario_actor': usuario_actor},
                              context_instance=RequestContext(request))

def asignar_horas_us (request, idUserStory):
    sprints = Sprint.objects.all()
    userstory = UserStory.objects.get(pk=idUserStory)
    return render_to_response('userstory/asignar_horas_us.html',{'sprints':sprints ,'userstory':userstory},context_instance=RequestContext(request))

def restar_horas_sprint (request, idSprint):
    mensaje = "Horas asiganadas correctamente"
    sprint = Sprint.objects.get (pk=idSprint)
    query = request.GET.get('q', '')
    print query 
    print sprint.Duracion
    sprint.Duracion = sprint.Duracion - int(query) 

    if(sprint.Duracion <= 0 ):
        sprint.Estado = 'Terminado'

        for us in sprint.UserStorys.all():
            us.Estado = 'Pendiente'
            us.save()

    sprint.save() 
    print sprint.Duracion 
    #sprint.Duracion = sprint.Duracion - request
    return render_to_response('userstory/operacion_userstory_exito.html',{'mensaje':mensaje},context_instance=RequestContext(request))



################################################################################################3


def avanzar_us(request, idUs):
    """
        Vista para hacer avanzar un us a travez de los estados y actividades de un flujo
            
        @type request: django.http.HttpRequest
        @param request: Contiene informacion sobre la solicitud web actual que llamo a esta vista  
        @type idUs : integer
        @param idUs : Contiene el id del User Story que se desea hacer avanzar.
        @rtype: django.shortcuts.render_to_response
        @return: retorn un HttpResponse a la pagina de notificacioin de exito
        @author: Cesar Recalde
    """
    us = UserStory.objects.get(pk = idUs)

    actividad = us.Actividad_asignada
    tabla = Flujo.objects.get(pk=actividad.idTabla)



    if( us.Estado_de_actividad == 'to_do' ):

        actividad.To_do.remove( us )
        us.Estado_de_actividad = 'doing'
        actividad.Doing.add(us)
        mensaje = "El user story a avanzado al estado 'doing' de la actividad " + actividad.Nombre

        
    elif( us.Estado_de_actividad == 'doing' ):

        actividad.Doing.remove( us )
        us.Estado_de_actividad = 'done'
        actividad.Done.add(us)
        mensaje = "El user story a avanzado al estado 'done' de la actividad " + actividad.Nombre

    elif( us.Estado_de_actividad == 'done' ):

        actividad.Done.remove( us )

        if( actividad.Orden == len( tabla.Actividades.all() ) ):
            us.Estado = 'Terminado'
            us.Estado_de_actividad = 'none'
            us.in_kanban = False
            mensaje = "El user story a completado el flujo y pasa al estado 'Terminado' "

        else:
            nueva_actividad = tabla.Actividades.get( Orden= (actividad.Orden +1) )
            nueva_actividad.To_do.add(us)
            us.Estado_de_actividad = 'to_do'
            us.Actividad_asignada = nueva_actividad
            nueva_actividad.save()
            mensaje = "El user story a avanzado al estado 'to_do' de la actividad " + nueva_actividad.Nombre

    us.save()
    actividad.save()
    tabla.save()

    return render_to_response('userstory/operacion_userstory_exito.html',{'mensaje':mensaje},context_instance=RequestContext(request))

def retroceder_us(request, idUs):

    """
        Vista para hacer retroceder un us al estado 'to_do' de la actividad precedente
            
        @type request: django.http.HttpRequest
        @param request: Contiene informacion sobre la solicitud web actual que llamo a esta vista  
        @type idUs : integer
        @param idUs : Contiene el id del User Story que se desea hacer retroceder.
        @rtype: django.shortcuts.render_to_response
        @return: retorn un HttpResponse a la pagina de notificacioin de exito
        @author: Cesar Recalde
    """

    us = UserStory.objects.get(pk = idUs)
    actividad = us.Actividad_asignada
    tabla = Flujo.objects.get(pk=actividad.idTabla)

    if(actividad.Orden == 1 and us.Estado_de_actividad == 'to_do'):
        mensaje = 'No se puede retroceder el us por que ya se encuentra en el primer estado de la primera actividad'
    else:

        if(actividad.Orden == 1):
            nueva_actividad = actividad
        else:
            nueva_actividad = tabla.Actividades.get(Orden = (actividad.Orden - 1) )

        actividad.To_do.remove(us)
        actividad.Doing.remove(us)
        actividad.Done.remove(us)
        actividad.save()

        nueva_actividad.To_do.add(us)
        us.Estado_de_actividad = 'to_do'

        us.save()
        nueva_actividad.save()

        mensaje = " Se retrocedio el us al estado 'to_do' de la actividad" + nueva_actividad.Nombre

    return render_to_response('userstory/operacion_userstory_exito.html',{'mensaje':mensaje},context_instance=RequestContext(request))
















