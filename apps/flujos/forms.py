from django.forms import ModelForm
from django import forms
from apps.roles.models import User, Group
from apps.proyectos.models import Proyecto
from .models import Flujo, Actividad





class FlujoForm(ModelForm):

    class Meta:
        model = Flujo
        exclude = ['Usuario' , 'Estado' , 'Usuario_creador' , 'Fecha_creacion']
        widgets = {'Actividades': forms.RadioSelect}


class ActividadForm(ModelForm):
	class Meta:
		model = Actividad

