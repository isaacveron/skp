from django.conf.urls import patterns, include, url
from .views import detalle_mcp

urlpatterns = patterns('',
     
	url(r'^detalle_mcp/(?P<idProyecto>\d+)/$', detalle_mcp),
	
)