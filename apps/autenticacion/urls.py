from django.conf.urls import patterns, include, url
from .views import iniciar_sesion, index, cerrar_sesion, crear_usuario, detalle_usuario, modificar_usuario, crear_rol, administrar_roles, detalle_rol
from django.contrib.auth.views import SetPasswordForm


urlpatterns = patterns('',
     
    url(r'^$', iniciar_sesion, name = 'home'),
    url(r'^index/$', index, name = 'index'),
    url(r'^nuevo_usuario/$', crear_usuario, name = 'crear_usuario'),
    url(r'^detalle_usuario/(?P<id_usuario_p>\d+)/$', detalle_usuario),	
	url(r'^modificar_usuario/$', modificar_usuario),
	url(r'^modificar/password/$', 'django.contrib.auth.views.password_change',
        {'current_app': 'app.autenticacion',
         'template_name': 'usuario/form_pass_usuario.html',
         'post_change_redirect': 'pass_done',
         'password_change_form': SetPasswordForm},
        name='password'),
	url(r'^modificar/password/done$', 'django.contrib.auth.views.password_change_done',
        {'template_name': 'usuario/operacion_usuario_exito_pass.html'}, name='pass_done'),
    url(r'^modificar_usuario/', include('django.contrib.auth.urls')),


    url(r'^crear_rol/$', crear_rol),
	url(r'^listar_roles/$', administrar_roles),
	url(r'^detalle_rol/(?P<idRol>\d+)/$', detalle_rol),
	

    url(r'^salir/$', cerrar_sesion, name='salir'),

)