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

# Create your views here.
@login_required(login_url = '/')
def gestion_de_sprint(request):
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
  sprints = Sprint.objects.all()
  return render_to_response('sprint/gestion_de_sprint.html',
                              {'usuario_actor': usuario_actor, 'sprints': sprints}, context_instance=RequestContext(request))


@login_required(login_url = '/')
@user_passes_test( User.can_add_proyecto , login_url="/index/")
def crear_sprint(request, idProyecto):
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
    mensaje="Sprint creado con exito"
    usuario_actor = request.user
    sprint = Sprint( Usuario_creador=usuario_actor, Proyecto_asignado=proyecto)

    if request.method == 'POST':
        formulario = SprintFormMod(request.POST, instance=sprint)
        if formulario.is_valid():
            formulario.save()
            sprints = Sprint.objects.all()
            return render_to_response('sprint/operacion_sprint_exito.html',
                                      {'mensaje': mensaje, 'usuario_actor': usuario_actor, 'sprints': sprint, 'proyecto':proyecto},
                                      context_instance=RequestContext(request))
    else:
        print sprint.Proyecto_asignado.id
        formulario = SprintForm(idProyecto=idProyecto)
    return render_to_response('sprint/crear_sprint.html',
                              {'formulario': formulario, 'operacion': 'Crear Sprint',
                               'usuario_actor': usuario_actor, 'proyecto':proyecto},
                              context_instance=RequestContext(request))

def detalle_sprint(request, idSprint):
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
    sprint = Sprint.objects.get(pk=idSprint)
    return render_to_response('sprint/detalle_sprint.html', {'usuario_actor': usuario_actor, 'sprint':sprint},
                              context_instance=RequestContext(request))

@login_required(login_url = '/')
def buscar_sprint(request):
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
        results = Sprint.objects.filter(qset).distinct()
    else:
        results = []
    return render_to_response('sprint/gestion_de_sprint.html', {'usuario_actor': usuario_actor, 'sprints': results}, context_instance=RequestContext(request))


@login_required(login_url = '/')
@user_passes_test( User.can_change_proyecto , login_url="/index/")
def modificar_sprint(request, idSprint):
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
    sprint = Sprint.objects.get(pk=idSprint)
    formulario = SprintFormMod(request.POST,instance=sprint)
    if formulario.is_valid():
        formulario.save()
        return HttpResponseRedirect('/gestion_de_sprint/')
    else:
        formulario = SprintFormMod(instance=sprint)
    return render_to_response('sprint/modificar_sprint.html',{'usuario_actor': usuario_actor, 'sprint':sprint, 'formulario':formulario},context_instance=RequestContext(request))


@login_required(login_url = '/')
def cambiar_estado_sprint(request, idSprint):
    mensaje = "Cambio de estado de Sprint con exito"
    sprint = Sprint.objects.get(pk=idSprint)
    if request.method == 'POST':
        formulario = SprintFormDelete(request.POST, instance=sprint)
        if formulario.is_valid():
           formulario.save()
           return render_to_response('sprint/operacion_sprint_exito.html',{'mensaje': mensaje}, context_instance=RequestContext(request))
    else:
        formulario = SprintFormDelete(instance=sprint)
    return render_to_response('sprint/eliminar_sprint.html',{'formulario': formulario},context_instance=RequestContext(request))

@login_required(login_url = '/')
@user_passes_test( User.can_delete_proyecto , login_url="/index/")
def vista_eliminar_sprint(request, idSprint):
    """
    Esta vista obtiene el proyecto que quiere ser eliminado, pregunta si quiere ser eliminado y llama 
    a la funcion eliminar_proyecto

    @param request: django.http.HttpRequest
    @param idProyecto: Contiene el identificador del proyecto a ser eliminado
    @return: se retorna la pagina de eliminacion de proyectos
    @author: Cesar Recalde
    """
    usuario_actor = request.user
    sprint = Sprint.objects.get(pk=idSprint)
    return render_to_response('sprint/eliminar_sprint.html', {'usuario_actor': usuario_actor, 'sprint': sprint}, context_instance=RequestContext(request))


@login_required(login_url = '/')
def eliminar_sprint(request, idSprint):
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

    mensaje = "Sprint eliminado con exito"
    sprint = Sprint.objects.get(pk=idSprint)
    sprint.delete()
    usuario_actor = request.user
    return render_to_response('sprint/operacion_sprint_exito.html',{'mensaje':mensaje, 'usuario_actor': usuario_actor}, context_instance=RequestContext(request))

