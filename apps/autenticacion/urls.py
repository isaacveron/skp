from django.conf.urls import patterns, include, url
from .views import iniciar_sesion, index, cerrar_sesion, nuevo_usuario

urlpatterns = patterns('',
     
    url(r'^$', iniciar_sesion, name = 'home'),
    url(r'^index/$', index, name = 'index'),
    url(r'^nuevo/$', nuevo_usuario, name = 'nuevo_usuario'),
    url(r'^salir/$', cerrar_sesion, name='salir'),

)