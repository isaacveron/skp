from django.conf.urls import patterns, include, url
from .views import crear_userstory, gestion_de_userstory, detalle_userstory, buscar_userstory, modificar_userstory, vista_eliminar_userstory, eliminar_userstory

urlpatterns = patterns('',
    url(r'^crear_userstory/(?P<idProyecto>\d+)/$', crear_userstory, name = 'crear_userstory'),
    url(r'^gestion_de_userstory/$', gestion_de_userstory, name = 'gestion_de_userstory'),
    url(r'^detalle_userstory/(?P<idUserStory>\d+)/$', detalle_userstory),
    url(r'^buscar_userstory/$', buscar_userstory),
    url(r'^modificar_userstory/(?P<idUserStory>\d+)/$', modificar_userstory),
    url(r'^eliminar_userstory/(?P<idUserStory>\d+)/$', vista_eliminar_userstory),
    url(r'^userstory_eliminado/(?P<idUserStory>\d+)/$', eliminar_userstory),
)	
 