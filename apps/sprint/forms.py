from django.forms import ModelForm
from django import forms
from apps.roles.models import User
from apps.sprint.models import Sprint
from apps.userstory.models import UserStory 
from apps.proyectos.models import Proyecto


class SprintForm(ModelForm):
    """
    Formulario para el la creacion de roles
    Hereda de forms.ModelForm y utiliza la clase Group para
    """
    
    def __init__(self, idProyecto, *args, **kwargs):
        usuarios = forms.ModelMultipleChoiceField(queryset=User.objects.none(), widget=forms.CheckboxSelectMultiple(), required=True)
        super(SprintForm, self).__init__(*args, **kwargs)
        #self.fields['UserStorys'] = forms.ChoiceField(choices=[ (o.id, str(o)) for o in Sprint.objects.filter(Proyecto_asignado=Proyecto_asignado)])       
        self.fields['UserStorys'].queryset = UserStory.objects.filter(Proyecto_asignado__id=idProyecto, is_active="True")
            
    class Meta:
        model = Sprint 
        exclude = ['is_active','Proyecto_asignado','Estado' , 'Usuario_creador' , 'Fecha_creacion']

class SprintFormDelete(ModelForm):    
    class Meta:
        model = Sprint
        fields=('is_active',)
            
class SprintFormMod(ModelForm):
    """
    Formulario para el la creacion de roles
    Hereda de forms.ModelForm y utiliza la clase Group para
    """
    
    def __init__(self, *args, **kwargs):
        super(SprintFormMod, self).__init__(*args, **kwargs)
        self.fields['UserStorys'].queryset = UserStory.objects.filter(Proyecto_asignado__id=self.instance.Proyecto_asignado.id)

    class Meta:
        model = Sprint 
        exclude = ['is_active','Proyecto_asignado','Estado' , 'Usuario_creador' , 'Fecha_creacion']