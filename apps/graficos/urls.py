from django.conf.urls import patterns, include, url
from .views import ver_burdownchart, ver_backlog, ver_burdownchart_proyecto

urlpatterns = patterns('',
    url(r'^ver_backlog/(?P<idSprint>\d+)/$', ver_backlog),
    url(r'^ver_burdownchart/(?P<idSprint>\d+)/$', ver_burdownchart),
    url(r'^ver_burdownchart_proyecto/(?P<idProyecto>\d+)/$', ver_burdownchart_proyecto),
)