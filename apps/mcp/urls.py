from django.conf.urls import patterns, include, url
from .views import detalle_mcp, vista_agregar_tabla, agregar_tabla, detalle_tabla

urlpatterns = patterns('',
     
	url(r'^detalle_mcp/(?P<idProyecto>\d+)/$', detalle_mcp),
	url(r'^vista_agregar_tabla/(?P<idProyecto>\d+)/$', vista_agregar_tabla),
	url(r'^agregar_tabla/(?P<idProyecto>\d+)/(?P<idTabla>\d+)/$', agregar_tabla),
	url(r'^detalle_tabla/(?P<idProyecto>\d+)/(?P<idTabla>\d+)/$', detalle_tabla),
)