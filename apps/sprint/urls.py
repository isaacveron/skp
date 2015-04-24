from django.conf.urls import patterns, include, url
from .views import crear_sprint, gestion_de_sprint, detalle_sprint, buscar_sprint, modificar_sprint

urlpatterns = patterns('',
    url(r'^crear_sprint/(?P<idProyecto>\d+)/$', crear_sprint, name = 'crear_sprint'),
    url(r'^gestion_de_sprint/$', gestion_de_sprint, name = 'gestion_de_sprint'),
    url(r'^detalle_sprint/(?P<idSprint>\d+)/$', detalle_sprint),
    url(r'^buscar_sprint/$', buscar_sprint),
    url(r'^modificar_sprint/(?P<idSprint>\d+)/$', modificar_sprint),
)	
 