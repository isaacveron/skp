from django.forms import ModelForm, SelectMultiple
from django import forms
from apps.roles.models import User, Group
from apps.userstory.models import UserStory
from apps.proyectos.models import Proyecto


class UserStoryForm(ModelForm):
    """
    Formulario para el la creacion de roles
    Hereda de forms.ModelForm y utiliza la clase Group para
    """
    #def __init__(self, *args, **kwargs):
        #super(UserStoryForm, self).__init__(*args, **kwargs)
        #self.fields['Usuario_asignado'].queryset = User.objects.filter(Usuario_asignado__Nombre='foo')
    class Meta:
        model = UserStory 
        exclude = ['Proyecto_asignado', 'Usuario_creador','Estado' , 'Usuario_creador' , 'Fecha_creacion']