from django.forms import ModelForm
from django import forms
from apps.roles.models import User, Group
from apps.proyectos.models import Proyecto
from apps.flujos.models import Flujo, Actividad





class ProyectoForm(ModelForm):
    """
    Formulario para el la creacion de roles
    Hereda de forms.ModelForm y utiliza la clase Group para
    """
    class Meta:
        model = Proyecto
        exclude = ['Usuario' , 'Estado' , 'Usuario_creador' , 'Fecha_creacion', 'Tablas']
    
    