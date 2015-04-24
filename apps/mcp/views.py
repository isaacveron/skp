from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.contrib.auth.models import User, Group, Permission
from django.contrib.auth.decorators import login_required, permission_required
from apps.proyectos.models import Proyecto
from apps.sprint.models import Sprint
from apps.userstory.models import UserStory

@login_required(login_url = '/')
def detalle_mcp(request, idProyecto):
    """
    Vista principal del sistema
    @rtype: django.http.HttpResponseRedirect
    @author: Isaac Veron
    """
    proyecto = Proyecto.objects.get(pk=idProyecto)
    sprints = Sprint.objects.all()
    usuario_actor = request.user
    userstorys = UserStory.objects.all()
	
    return render_to_response('mcp/detalle_mcp.html', {'usuario_actor': usuario_actor, 'proyecto':proyecto, 'userstorys':userstorys, 'sprints':sprints},
                              context_instance=RequestContext(request))