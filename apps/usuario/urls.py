from django.conf.urls import patterns, include, url
from .views import iniciar_sesion, index, cerrar_sesion, crear_usuario, detalle_usuario, modificar_usuario, administrar_usuario, asignar_rol, vista_eliminar_usuario, eliminar_usuario, buscar_usuario
from django.contrib.auth.views import SetPasswordForm

urlpatterns = patterns('',
     
    url(r'^$', iniciar_sesion, name = 'home'),
    url(r'^index/$', index, name = 'index'),
    url(r'^nuevo_usuario/$', crear_usuario, name = 'crear_usuario'),
    url(r'^listar_usuarios/$', administrar_usuario, name = 'crear_usuario'),
    url(r'^detalle_usuario/(?P<idUsuario>\d+)/$', detalle_usuario),	
	url(r'^modificar_usuario/(?P<idUsuario>\d+)/$', modificar_usuario),
    url(r'^password/change$', 'django.contrib.auth.views.password_change', {'template_name': 'usuario/password_change_form.html'}, name="password_change"),
	url(r'^password/$', 'django.contrib.auth.views.password_change_done', {'template_name': 'usuario/password_change_done.html'}, name="password_change_done"),
    url(r'^modificar_usuario/$', include('django.contrib.auth.urls')),
    url(r'^vista_eliminar_usuario/(?P<idUsuario>\d+)/$', vista_eliminar_usuario),
    url(r'^usuario_eliminado/(?P<idUsuario>\d+)/$', eliminar_usuario),
    url(r'^asignado/(?P<idRol>\d+)$', asignar_rol),
    url(r'^search_user/$', buscar_usuario),
    url(r'^salir/$', cerrar_sesion, name='salir'),

)
"""
url(r'^modificar/password/$', 'django.contrib.auth.views.password_change',
        {'current_app': 'app.autenticacion',
         'template_name': 'usuario/form_pass_usuario.html',
         'post_change_redirect': 'pass_done',
         'password_change_form': SetPasswordForm},
        name='password'),
    url(r'^modificar/password/done$', 'django.contrib.auth.views.password_change_done',
        {'template_name': 'usuario/operacion_usuario_exito_pass.html'}, name='pass_done'),
"""