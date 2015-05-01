from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'skp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('apps.usuario.urls')),
    url(r'^', include('apps.roles.urls')),
    url(r'^', include('apps.proyectos.urls')),
    url(r'^', include('apps.flujos.urls')),
    url(r'^', include('apps.sprint.urls')),
    url(r'^', include('apps.userstory.urls')),
    url(r'^', include('apps.mcp.urls')),
)
