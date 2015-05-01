from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.contrib.auth.models import User, Group, Permission
from django.contrib.auth.decorators import login_required, permission_required
from apps.proyectos.models import Proyecto
from apps.sprint.models import Sprint
from apps.userstory.models import UserStory
from apps.flujos.models import Flujo, Actividad

@login_required(login_url = '/')
def detalle_mcp(request, idProyecto):
    """
        Recibe un request, obtiene la lista de todos los userstorys y sprints
        del sistema y luego retorna el html renderizado con los datos 

        @type request: django.http.HttpRequest
        @param request: Contiene informacion sobre la solic. web actual que llamo a esta vista
        @param idProyecto: identificador del proyecto cuyos datos desean verse 
        @rtype: django.http.HttpResponse
        @return: detalle_mcp.html, donde se muestarn los datos del proyecto
        @author: Cesar Recalde
    """
    proyecto = Proyecto.objects.get(pk=idProyecto)
    sprints = Sprint.objects.all()
    usuario_actor = request.user
    userstorys = UserStory.objects.all()
    tablas = proyecto.Tablas.all()
	
    return render_to_response('mcp/detalle_mcp.html', {'usuario_actor': usuario_actor, 'proyecto':proyecto, 'userstorys':userstorys, 'sprints':sprints,'tablas':tablas},
                              context_instance=RequestContext(request))


@login_required(login_url = '/')
def detalle_tabla(request, idProyecto, idTabla):

    """
        Recibe un request, obtiene los datos de la tabla solicitada y muestra sus actividades y
        userstorys en ellas

        @type request: django.http.HttpRequest
        @param request: Contiene informacion sobre la solic. web actual que llamo a esta vista
        @param idProyecto: identificador del proyecto al que pertenece la tabla
        @param idTabla: identificador de la tabla  
        @rtype: django.http.HttpResponse
        @return: detalle_tabla.html, donde se muestarn los datos de la tabla
        @author: Cesar Recalde
    """
    tabla = Flujo.objects.get(pk=idTabla)
    actividades = tabla.Actividades.all()
    usuario_actor = request.user
    proyecto = Proyecto.objects.get(pk=idProyecto)

    return render_to_response('mcp/detalle_tabla.html', {'usuario_actor': usuario_actor, 'proyecto':proyecto,'tabla':tabla, 'actividades':actividades},
                              context_instance=RequestContext(request))

@login_required(login_url = '/')
def vista_agregar_tabla(request, idProyecto):
    """
        Recibe un request, y el identificador del proyecto al que se desea agregar la tabla,
        obtiene la lista de las tablas disponibles y las despliega para que el usuario pueda
        seleccionar una

        @type request: django.http.HttpRequest
        @param request: Contiene informacion sobre la solic. web actual que llamo a esta vista
        @param idProyecto: identificador del proyecto al que se desea agregar la tabla 
        @rtype: django.http.HttpResponse
        @return: vista_agregar_tabla.html, donde se muestarn los flujos del sistema
        @author: Cesar Recalde
    """

    usuario_actor = request.user
    proyecto = Proyecto.objects.get(pk=idProyecto)
    tablas = Flujo.objects.filter(Copia = False)

    for aux in proyecto.Tablas.all() :
        tablas = tablas.exclude(Nombre = aux.Nombre)

    return render_to_response('mcp/vista_agregar_tabla.html', {'usuario_actor': usuario_actor, 'tablas':tablas, 'proyecto':proyecto},
                              context_instance=RequestContext(request))



@login_required(login_url = '/')
def agregar_tabla(request, idProyecto, idTabla):

    """
        Recibe un request,el identificador del proyecto y el identificador de la tabla 
        que desea agregarse

        @type request: django.http.HttpRequest
        @param request: Contiene informacion sobre la solic. web actual que llamo a esta vista
        @param idProyecto: identificador del proyecto al que se desea agregar la tabla 
        @param idTabla: identificador de la tabla que se desea agregar  
        @rtype: django.http.HttpResponse
        @return: agregar_tabla_exito.html, vista donde se muestra un mensaje dde exito de la operacion
        @author: Cesar Recalde
    """
    usuario_actor = request.user
    tabla = Flujo.objects.get(pk=idTabla)
    proyecto = Proyecto.objects.get(pk=idProyecto)
    mensaje = 'Tabla agregada con exito'

    proyecto.Tablas.add(tabla)
    proyecto.save()

    return render_to_response('mcp/agregar_tabla_exito.html', {'mensaje':mensaje,'usuario_actor': usuario_actor, 'tabla':tabla, 'proyecto':proyecto},
                              context_instance=RequestContext(request))

