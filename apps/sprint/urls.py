from django.conf.urls import patterns, include, url
from .views import crear_sprint, gestion_de_sprint, detalle_sprint, buscar_sprint, modificar_sprint
from .views import vista_eliminar_sprint, eliminar_sprint, cambiar_estado_sprint
from .views import vista_iniciar_sprint, iniciar_sprint, vista_detener_sprint, detener_sprint

urlpatterns = patterns('',
    url(r'^crear_sprint/(?P<idProyecto>\d+)/$', crear_sprint, name = 'crear_sprint'),
    url(r'^gestion_de_sprint/$', gestion_de_sprint, name = 'gestion_de_sprint'),
    url(r'^detalle_sprint/(?P<idSprint>\d+)/$', detalle_sprint),
    url(r'^buscar_sprint/$', buscar_sprint),
    url(r'^modificar_sprint/(?P<idSprint>\d+)/$', modificar_sprint),
    url(r'^cambiar_estado_sprint/(?P<idSprint>\d+)/$', cambiar_estado_sprint),
    url(r'^vista_eliminar_sprint/(?P<idSprint>\d+)/$', vista_eliminar_sprint),
    url(r'^sprint_eliminado/(?P<idSprint>\d+)/$', eliminar_sprint),
    url(r'^vista_iniciar_sprint/(?P<idSprint>\d+)/$', vista_iniciar_sprint),
    url(r'^iniciar_sprint/(?P<idSprint>\d+)/$', iniciar_sprint),
    url(r'^detener_sprint/(?P<idSprint>\d+)/$', detener_sprint),
    url(r'^vista_detener_sprint/(?P<idSprint>\d+)/$', vista_detener_sprint),
)	
 