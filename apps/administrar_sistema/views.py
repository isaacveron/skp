from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext

# Create your views here.


def gestion_de_proyectos(request):
    return render_to_response('administrar_sistema/gestion_de_proyectos.html', context_instance = RequestContext(request))

def gestion_de_roles(request):
    return render_to_response('administrar_sistema/gestion_de_roles.html', context_instance = RequestContext(request))

