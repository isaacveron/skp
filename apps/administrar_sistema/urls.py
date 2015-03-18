from django.conf.urls import patterns, include, url
from .views import gestion_de_proyectos, gestion_de_roles

urlpatterns = patterns('',
     
    url(r'^gestion_de_proyectos', gestion_de_proyectos, name = 'gestion_de_proyectos'),
    url(r'^gestion_de_roles', gestion_de_roles, name = 'gestion_de_roles'),
   
)