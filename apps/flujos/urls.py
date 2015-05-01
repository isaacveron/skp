from django.conf.urls import patterns, include, url
from .views import crear_flujo, administrar_flujos, detalle_flujo, buscar_flujo, modificar_flujo
from .views import vista_eliminar_flujo, eliminar_flujo

urlpatterns = patterns('',
    url(r'^crear_flujo/$', crear_flujo, name = 'crear_flujo'),
    url(r'^administrar_flujos', administrar_flujos, name = 'administrar_flujos'),
    url(r'^detalle_flujo/(?P<idFlujo>\d+)/$', detalle_flujo),
    url(r'^buscar_flujo/$', buscar_flujo),
    url(r'^modificar_flujo/(?P<idFlujo>\d+)/$', modificar_flujo),
    url(r'^vista_eliminar_flujo/(?P<idFlujo>\d+)/$', vista_eliminar_flujo),
    url(r'^flujo_eliminado/(?P<idFlujo>\d+)/$', eliminar_flujo),
)	