from django.forms import ModelForm
from django import forms
from apps.roles.models import User, Group
from apps.sprint.models import Sprint
from apps.userstory.models import UserStory 
from apps.proyectos.models import Proyecto


class SprintForm(ModelForm):
    """
    Formulario para el la creacion de roles
    Hereda de forms.ModelForm y utiliza la clase Group para
    """
    
    def __init__(self, *args, **kwargs):
        super(SprintForm, self).__init__(*args, **kwargs)
        self.fields['UserStorys'].queryset = UserStory.objects.filter(Proyecto_asignado__id=2)
    
    class Meta:
        model = Sprint 
        exclude = ['Proyecto_asignado','Estado' , 'Usuario_creador' , 'Fecha_creacion']
    
    