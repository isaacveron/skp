from django.conf.urls import patterns, include, url
from .views import crear_proyecto, gestion_de_proyectos, detalle_proyecto


urlpatterns = patterns('',
     
    url(r'^crear_proyecto/$', crear_proyecto, name = 'crear_proyecto'),
    url(r'^gestion_de_proyectos', gestion_de_proyectos, name = 'gestion_de_proyectos'),
    url(r'^detalle_proyecto/(?P<idProyecto>\d+)/$', detalle_proyecto),
)	