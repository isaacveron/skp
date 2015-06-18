from django.shortcuts import render, render_to_response
from django.template import RequestContext
from apps.archivos.models import Document
from apps.userstory.models import CargarHoras
from apps.archivos.forms import DocumentForm
# Create your views here.
from django.views.generic.edit import CreateView

def vista_adjuntar_archivo(request):
   
    usuario_actor = request.user
    #horas_us = CargarHoras.objects.get(pk=id_Horas)
    doc = Document()
    if request.method == 'POST':
    	print "holaa"
        formulario = DocumentForm(request.POST)
        if formulario.is_valid():
            formulario.save()

            #adjuntar_archivo(formulario.instance.pk, horas_us.id)

            return render_to_response('userstory/operacion_userstory_exito.html',
                                      {'usuario_actor': usuario_actor},context_instance=RequestContext(request))
    else:
        formulario = DocumentForm()
    return render_to_response('archivos/document_form.html', {'formulario': formulario, 'usuario_actor': usuario_actor},context_instance=RequestContext(request))


def adjuntar_archivo(id_Document, id_Horas):
	usuario_actor = request.user
	archivo = Document.objects.get(pk=id_Document)
	horas_us = CargarHoras.objects.get(pk=id_Horas)

	horas_us.Archivos_adjuntos.add(archivo)
	horas_us.save()
	
	print "Oiko kp"