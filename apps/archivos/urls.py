from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from apps.archivos.views import vista_adjuntar_archivo
# project imports
from apps.archivos.forms import DocumentForm
from apps.archivos.models import Document


urlpatterns = patterns('',
	url(r'^files/', include('db_file_storage.urls')),
	
	url(r'^lista_archivos_adjunto', ListView.as_view(queryset=Document.objects.all(),template_name='archivos/document_list.html'),name='document.list'),
	url(r'^add_archivo_adjunto/$', CreateView.as_view(model=Document, form_class=DocumentForm, template_name='archivos/document_form.html', success_url=reverse_lazy('document.list')),name='document.add'),
	url(r'^edit_archivo_adjunto/(?P<pk>\d+)/$', UpdateView.as_view( model=Document,form_class=DocumentForm,template_name='archivos/document_form.html', success_url=reverse_lazy('document.list')),name='document.edit'),
	url(r'^delete_archivo_adjunto/(?P<pk>\d+)/$', DeleteView.as_view(model=Document, success_url=reverse_lazy('document.list')),name='document.delete'),
)

#url(r'^add_archivo_adjunto/$', CreateView.as_view(model=Document, form_class=DocumentForm, template_name='archivos/document_form.html', success_url=reverse_lazy('document.list')),name='document.add'),
	