from django.conf.urls import patterns, include, url
from .views import crear_proyecto, gestion_de_proyectos, detalle_proyecto, buscar_proyecto, modificar_proyecto
from .views import vista_eliminar_proyecto, eliminar_proyecto

urlpatterns = patterns('',
     
    url(r'^crear_proyecto/$', crear_proyecto, name = 'crear_proyecto'),
    url(r'^gestion_de_proyectos', gestion_de_proyectos, name = 'gestion_de_proyectos'),
    url(r'^detalle_proyecto/(?P<idProyecto>\d+)/$', detalle_proyecto),
    url(r'^buscar_proyecto/$', buscar_proyecto),
    url(r'^modificar_proyecto/(?P<idProyecto>\d+)/$', modificar_proyecto),
    url(r'^vista_eliminar_proyecto/(?P<idProyecto>\d+)/$', vista_eliminar_proyecto),
    url(r'^proyecto_eliminado/(?P<idProyecto>\d+)/$', eliminar_proyecto),

)	