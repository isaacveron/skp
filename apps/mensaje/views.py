from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from apps.usuario.models import User
from apps.mensaje.models import Mensaje
from apps.mensaje.forms import MensajeForm
from django.core.mail import send_mail

# Create your views here.
def enviar_mensaje(request):
	usuario_actor = request.user
	mensaje = Mensaje(Usuario_que_envio=usuario_actor)
	if request.method == 'POST':
		formulario = MensajeForm(request.POST, instance=mensaje)
		if formulario.is_valid():
			formulario.save()
			send_mail('test email', formulario.instance.Contenido_mensaje, 'is2skp@gmail.com', [formulario.instance.Usuario_a_enviar.email])
			return render_to_response('mensaje/operacion_exito.html', context_instance=RequestContext(request))
	else:
		formulario = MensajeForm()
	return render_to_response ('mensaje/enviar_mensaje.html',{'formulario':formulario, 'usuario_actor':usuario_actor}, context_instance=RequestContext(request))
    