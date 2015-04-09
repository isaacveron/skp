from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User, Group
from .models import Proyecto





class ProyectoForm(ModelForm):
    """
    Formulario para el la creacion de roles
    Hereda de forms.ModelForm y utiliza la clase Group para
    """
    class Meta:
        model = Proyecto
        exclude = ['Usuario' , 'Estado' , 'Usuario_creador' , 'Fecha_creacion']
        