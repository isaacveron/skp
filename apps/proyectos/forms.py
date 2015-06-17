from django.forms import ModelForm
from django import forms
from apps.roles.models import User, Group
from apps.proyectos.models import Proyecto
from apps.flujos.models import Flujo, Actividad
from django.forms.widgets import Select, Widget
from django.forms import extras



class ProyectoForm(ModelForm):
    """
    Formulario para el la creacion de roles
    Hereda de forms.ModelForm y utiliza la clase Group para
    """

    class Meta:
        model = Proyecto
        exclude = ['Restante','sprint_activo','Duracion','Registro','Dia_actual','Usuario','Estado',
        			'Usuario_creador' , 'Fecha_creacion', 'Tablas']
    	widgets = {'Fecha_inicio': forms.extras.widgets.SelectDateWidget() ,'Fecha_finalizacion':forms.extras.widgets.SelectDateWidget()}
    