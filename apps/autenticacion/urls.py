from django.conf.urls import patterns, include, url
from .views import iniciar_sesion, index, cerrar_sesion

urlpatterns = patterns('',
     
    url(r'^$', iniciar_sesion, name = 'home'),
    url(r'^index/$', index, name = 'index'),
    url(r'^salir/$', cerrar_sesion, name='salir'),

)