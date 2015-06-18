from django.conf.urls import patterns, include, url
from .views import reporte, descargar_reporteUsuarios

urlpatterns = patterns('',
	url(r"^reporte/$", reporte),
	url(r'^reporte/usuarios/$',descargar_reporteUsuarios),
)