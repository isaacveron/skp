from django.forms import ModelForm
from django import forms
#from django.contrib.auth.models import Group, User
from apps.usuario.models import User
from apps.roles.models import Group

class RolForm(forms.ModelForm):
    """
    Formulario para el la creacion de roles
    Hereda de forms.ModelForm y utiliza la clase Group para
    """
    class Meta:
        model = Group
        exclude = ['Usuario']

class AsignarRol(forms.ModelForm):
    """
    Formulario para la asignacion de roles a los usuarios
    Hereda del forms.ModelForm y utiliza la clase user
    para agregar ciertos campos de la clase a la hora de la asignacion
    """
    class Meta:
        model = User
        fields = ('groups',)