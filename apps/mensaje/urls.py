from django.conf.urls import patterns, include, url
from .views import enviar_mensaje

urlpatterns = patterns('',
     
    url(r'^enviar_mensaje/$', enviar_mensaje, name = 'enviar_mensaje'),
)	