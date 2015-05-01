from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from apps.roles.models import User, Group
from apps.flujos.models import Flujo, Actividad
from apps.flujos.forms import FlujoForm, ActividadForm, ActividadFormSet
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.decorators import user_passes_test
from django.db.models import Q
from django import forms

# Create your views here.


@login_required(login_url = '/')
def administrar_flujos(request):
    """
    Recibe un request, obtiene la lista de todos los flujos del sistema y 
    luego retorna el html renderizado con la lista de flujos

    @type request: django.http.HttpRequest
    @param request: Contiene informacion sobre la solic. web actual que llamo a esta vista
    @rtype: django.http.HttpResponse
    @return: administrar_flujo.html, donde se listan los flujos   
    @author: Cesar recalde
    """

    usuario_actor = request.user
    flujos = Flujo.objects.all()
    return render_to_response('flujo/administrar_flujos.html',
                              {'usuario_actor': usuario_actor, 'flujos': flujos}, context_instance=RequestContext(request))



@login_required(login_url = '/')
@user_passes_test( User.can_add_flujo , login_url="/index/")
def crear_flujo(request):
    """
     Vista de creacion de nuevo Flujo
    Recibe como parametro un request y retorna la pagina web crear_flujo.html donde se debe completar
    los datos del flujo y luego operacion_flujo_exito.html si se completo debidamente el formulario
    * Variables
        -usuario_actor: es el usuario que realiza la accion
        -formulario: es el fomrulario que debe completar el usuario_actor
        -flujos: es la lista de flujos existentes en el sistema
    @type request: django.http.HttpRequest
    @param request: Contiene informacion sobre la solic. web actual que llamo a esta vista  
    @rtype: django.http.HttpResponse
    @return: operacion_flujo_exito.html, mensaje de exito
    @author: Cesar Recalde
    """
    mensaje="Flujo creado con exito"
    usuario_actor = request.user
    flujo = Flujo( Usuario_creador=usuario_actor)

    if request.method == 'POST':
        formulario = FlujoForm(request.POST, instance=flujo)

        if formulario.is_valid():

            flujo_creado = formulario.save()

            nombresActividades = request.POST.getlist('nombreActividad')

            i=1
            
            for nombre in nombresActividades:
            	actividad = Actividad(Nombre=nombre, Orden=i, idTabla=flujo_creado.id)
            	actividad.save()
            	flujo_creado.Actividades.add(actividad)
            	flujo_creado.save()
            	i = i + 1
            	
            flujos = Flujo.objects.all()
            return render_to_response('flujo/operacion_flujo_exito.html',
                                      {'mensaje': mensaje, 'usuario_actor': usuario_actor, 'flujos': flujos},
                                      context_instance=RequestContext(request))
    else:
        formulario = FlujoForm()
    return render_to_response('flujo/crear_flujo.html',
                              {'formulario': formulario, 'operacion': 'Crear Flujo',
                               'usuario_actor': usuario_actor},
                              context_instance=RequestContext(request))

def detalle_flujo(request, idFlujo):
    """ 
      Busca en la base de datos al flujo cuyos datos se quieren consultar y los presenta en un vista html
    
      @type request: django.http.HttpRequest
      @param request: Contiene informacion sobre la solic. web actual que llamo a esta vista
      @type idFlujo: integer
      @param idFlujo: es el id del flujo cuyos datos se quieren consultar
      @rtype: django.HttpResponse
      @return: detalle_flujo.html, donde se le despliega al usuario los datos
      @author: Cesar Recalde
    """
    usuario_actor = request.user
    flujo = Flujo.objects.get(pk=idFlujo)
    return render_to_response('flujo/detalle_flujo.html', {'usuario_actor': usuario_actor, 'flujo': flujo},
                              context_instance=RequestContext(request))

@login_required(login_url = '/')
def buscar_flujo(request):
    """
    Vista para buscar un flujo dentro del listado de flujos del sistema

    @return: Se retorna a la pagina de vista de flujos con el flujo que coincida con el query o vacio
    @author: Cesar Recalde
    """
    usuario_actor = request.user
    query = request.GET.get('q', '')
    if query:
        qset = (
            Q(Nombre=query)
        )
        results = Flujo.objects.filter(qset).distinct()
    else:
        results = []
    return render_to_response('flujo/administrar_flujos.html', {'usuario_actor': usuario_actor, 'flujos': results}, context_instance=RequestContext(request))


@login_required(login_url = '/')
@user_passes_test( User.can_change_flujo , login_url="/index/")
def modificar_flujo(request, idFlujo):
    """
    Busca en la base de datos el flujo cuyos datos se quieren modificar.
    Presenta esos datos en un formulario y luego se guardan los cambios realizados.
     
    @type request: django.http.HttpRequest
    @param request: Contiene informacion sobre la solic. web actual que llamo a esta vista
    @type idFlujo: integer
    @param idFlujo: es el id del flujo cuyos datos se quieren modificar
    @rtype: django.HttpResponse
    @return: modificar_flujo.html,un formulario donde se despliegan los datos que el usuario puede modificar,
    una vez modificado renderiza a la pagina donde se listan todos los flujos
    @author: Cesar Recalde
    """

    usuario_actor = request.user
    flujo = Flujo.objects.get(pk=idFlujo)
    formulario = FlujoForm(request.POST, instance=flujo)
    if formulario.is_valid():
        formulario.save()
        return HttpResponseRedirect('/administrar_flujos/')
    else:
        formulario = FlujoForm( instance=flujo )
    return render_to_response('flujo/modificar_flujo.html',
                              {'usuario_actor': usuario_actor, 'flujo':flujo, 'formulario':formulario},
                              context_instance=RequestContext(request))



@login_required(login_url = '/')
@user_passes_test( User.can_delete_flujo , login_url="/index/")
def vista_eliminar_flujo(request, idFlujo):
    """
    Esta vista obtiene el flujo que quiere ser eliminado, pregunta si quiere ser eliminado y llama 
    a la funcion eliminar_flujo

    @param request: django.http.HttpRequest
    @param idFlujo: Contiene el identificador del flujo a ser eliminado
    @return: se retorna la pagina de eliminacion de flujos
    @author: Cesar Recalde
    """
    usuario_actor = request.user
    flujo = Flujo.objects.get(pk=idFlujo)
    return render_to_response('flujo/eliminar_flujo.html', {'usuario_actor': usuario_actor, 'flujo': flujo},
                              context_instance=RequestContext(request))

@login_required(login_url = '/')
def eliminar_flujo(request, idFlujo):
    """
    Eliminar de manera logica los registros del flujo.
        
    @type request: django.http.HttpRequest
    @param request: Contiene informacion sobre la solicitud web actual que llamo a esta vista  
    @type idFlujo: integer
    @param idFlujo : Contiene el id del flujo a ser eliminado.
    @rtype: django.shortcuts.render_to_response
    @return: Se retorna a la a la pagina de notificacion de exito
    @author: Cesar Recalde
    """

    mensaje = "Flujo eliminado con exito"
    flujo = Flujo.objects.get(pk=idFlujo)
    flujo.delete()
    usuario_actor = request.user
    flujos = Flujo.objects.all()
    return render_to_response('flujo/operacion_flujo_exito.html',
                              {'mensaje':mensaje, 'usuario_actor': usuario_actor, 'flujos': flujos},
                              context_instance=RequestContext(request))



#########################################################################################
