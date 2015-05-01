from django.forms import ModelForm
from django import forms
from apps.roles.models import User, Group
from apps.proyectos.models import Proyecto
from .models import Flujo, Actividad
from django.forms.formsets import formset_factory
from django.contrib.admin.widgets import FilteredSelectMultiple

class ActividadForm(ModelForm):
	Nombre = forms.CharField()

ActividadFormSet = formset_factory(ActividadForm)

class FlujoForm(ModelForm):

    class Meta:
        model = Flujo
        exclude = ['Usuario' , 'Estado' , 'Usuario_creador' , 'Fecha_creacion', 'Actividades', 'Copia']
        #widgets = {'Actividades': forms.SelectMultiple}

