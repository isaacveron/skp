from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from apps.proyectos.forms import ProyectoForm
from apps.roles.models import Group
from apps.usuario.models import User
from apps.proyectos.models import Proyecto
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.decorators import user_passes_test
from django.db.models import Q

# Create your views here.
@login_required(login_url = '/')
def gestion_de_proyectos(request):
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
  proyectos = Proyecto.objects.all()
  return render_to_response('proyecto/gestion_de_proyectos.html',
                              {'usuario_actor': usuario_actor, 'proyectos': proyectos}, context_instance=RequestContext(request))


@login_required(login_url = '/')
@user_passes_test( User.can_add_proyecto , login_url="/index/")
def crear_proyecto(request):
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
    mensaje="Proyecto creado con exito"
    usuario_actor = request.user
    proyecto = Proyecto( Usuario_creador=usuario_actor)
    if request.method == 'POST':
        formulario = ProyectoForm(request.POST, instance=proyecto)
        if formulario.is_valid():
            formulario.save()
            proyectos = Proyecto.objects.all()
            return render_to_response('proyecto/operacion_proyecto_exito.html',
                                      {'mensaje': mensaje, 'usuario_actor': usuario_actor, 'proyectos': proyectos},
                                      context_instance=RequestContext(request))
    else:
        formulario = ProyectoForm()
    return render_to_response('proyecto/crear_proyecto.html',
                              {'formulario': formulario, 'operacion': 'Crear Proyecto',
                               'usuario_actor': usuario_actor},
                              context_instance=RequestContext(request))


def detalle_proyecto(request, idProyecto):
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
    proyecto = Proyecto.objects.get(pk=idProyecto)
    return render_to_response('proyecto/detalle_proyecto.html', {'usuario_actor': usuario_actor, 'proyecto': proyecto},
                              context_instance=RequestContext(request))

@login_required(login_url = '/')
def buscar_proyecto(request):
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
        results = Proyecto.objects.filter(qset).distinct()
    else:
        results = []
    return render_to_response('proyecto/gestion_de_proyectos.html', {'usuario_actor': usuario_actor, 'proyectos': results}, context_instance=RequestContext(request))


@login_required(login_url = '/')
@user_passes_test( User.can_change_proyecto , login_url="/index/")
def modificar_proyecto(request, idProyecto):
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
    proyecto = Proyecto.objects.get(pk=idProyecto)
    formulario = ProyectoForm(request.POST, instance=proyecto)
    if formulario.is_valid():
        formulario.save()
        return HttpResponseRedirect('/gestion_de_proyectos/')
    else:
        formulario = ProyectoForm( instance=proyecto )
    return render_to_response('proyecto/modificar_proyecto.html',
                              {'usuario_actor': usuario_actor, 'proyecto':proyecto, 'formulario':formulario},
                              context_instance=RequestContext(request))


@login_required(login_url = '/')
@user_passes_test( User.can_delete_proyecto , login_url="/index/")
def vista_eliminar_proyecto(request, idProyecto):
    """
    Esta vista obtiene el proyecto que quiere ser eliminado, pregunta si quiere ser eliminado y llama 
    a la funcion eliminar_proyecto

    @param request: django.http.HttpRequest
    @param idProyecto: Contiene el identificador del proyecto a ser eliminado
    @return: se retorna la pagina de eliminacion de proyectos
    @author: Cesar Recalde
    """
    usuario_actor = request.user
    proyecto = Proyecto.objects.get(pk=idProyecto)
    return render_to_response('proyecto/eliminar_proyecto.html', {'usuario_actor': usuario_actor, 'proyecto': proyecto},
                              context_instance=RequestContext(request))


@login_required(login_url = '/')
def eliminar_proyecto(request, idProyecto):
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

    mensaje = "Proyecto eliminado con exito"
    proyecto = Proyecto.objects.get(pk=idProyecto)
    proyecto.delete()
    usuario_actor = request.user
    proyectos = Proyecto.objects.all()
    return render_to_response('proyecto/operacion_proyecto_exito.html',
                              {'mensaje':mensaje, 'usuario_actor': usuario_actor, 'proyectos': proyectos},
                              context_instance=RequestContext(request))
