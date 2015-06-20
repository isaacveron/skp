from django.conf.urls import patterns, include, url
from .views import reportes, vista_reporte_seis
from .views import llamada_reporte_uno, llamada_reporte_dos, llamada_reporte_tres, llamada_reporte_cuatro, llamada_reporte_cinco, llamada_reporte_seis
from .views import ver_reporte_uno, ver_reporte_dos, ver_reporte_tres, ver_reporte_cuatro, ver_reporte_cinco

urlpatterns = patterns('',
	url(r'^reportes/$',reportes),
	url(r'^reportes/(?P<idSprint>\d+)/$',vista_reporte_seis),
	url(r'^reportes/uno/$',llamada_reporte_uno),
	url(r'^reportes/dos/$',llamada_reporte_dos),
	url(r'^reportes/tres/$',llamada_reporte_tres),
	url(r'^reportes/cuatro/$',llamada_reporte_cuatro),
	url(r'^reportes/cinco/$',llamada_reporte_cinco),
	url(r'^reportes/seis/$',llamada_reporte_seis),
	url(r'^ver_reportes/uno/$',ver_reporte_uno),
	url(r'^ver_reportes/dos/$',ver_reporte_dos),
	url(r'^ver_reportes/tres/$',ver_reporte_tres),
	url(r'^ver_reportes/cuatro/$',ver_reporte_cuatro),
	url(r'^ver_reportes/cinco/$',ver_reporte_cinco),
)