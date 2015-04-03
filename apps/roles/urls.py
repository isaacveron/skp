from django.conf.urls import patterns, include, url
from .views import gestion_de_proyectos, crear_rol, administrar_roles, detalle_rol, modificar_rol, vista_eliminar_rol, eliminar_rol

urlpatterns = patterns('',
     
    url(r'^gestion_de_proyectos', gestion_de_proyectos, name = 'gestion_de_proyectos'),
    url(r'^crear_rol/$', crear_rol),
	url(r'^listar_roles/$', administrar_roles),
	url(r'^detalle_rol/(?P<idRol>\d+)/$', detalle_rol),
	url(r'^modificar_rol/(?P<idRol>\d+)/$', modificar_rol),
    url(r'^vista_eliminar_rol/(?P<idRol>\d+)/$', vista_eliminar_rol),
    url(r'^rol_eliminado/(?P<idRol>\d+)/$', eliminar_rol),	
)