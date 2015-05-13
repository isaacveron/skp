from django.forms import ModelForm
from django import forms
from apps.roles.models import User
from apps.sprint.models import Sprint
from apps.userstory.models import UserStory 
from apps.proyectos.models import Proyecto


class SprintForm(ModelForm):
    """
    Formulario para el la creacion de sprints
    Hereda de forms.ModelForm
    """
    
    def __init__(self, idProyecto, *args, **kwargs):
        
        super(SprintForm, self).__init__(*args, **kwargs)
        self.fields['UserStorys'].queryset = UserStory.objects.filter(Proyecto_asignado__id=idProyecto, is_active="True", Estado="Pendiente" )
        self.fields['Tabla_asignada'].queryset = Proyecto.objects.get(pk=idProyecto).Tablas.all()

    class Meta:
        model = Sprint 
        exclude = ['Duracion','is_active','Proyecto_asignado','Estado' , 'Usuario_creador' , 'Fecha_creacion']
           
class SprintFormMod(ModelForm):
    """
    Formulario para el la creacion de roles
    Hereda de forms.ModelForm y utiliza la clase Group para
    """
    
    def __init__(self, *args, **kwargs):
        super(SprintFormMod, self).__init__(*args, **kwargs)
        self.fields['UserStorys'].queryset = UserStory.objects.filter(Proyecto_asignado__id=self.instance.Proyecto_asignado.id,  is_active="True")
        self.fields['Tabla_asignada'].queryset = Proyecto.objects.get(pk=self.instance.Proyecto_asignado.id).Tablas.all()
    class Meta:
        model = Sprint 
        exclude = ['Duracion','is_active','Proyecto_asignado','Estado' , 'Usuario_creador' , 'Fecha_creacion']

class SprintFormDelete(ModelForm):    
    class Meta:
        model = Sprint
        fields=('is_active',)
#usuarios = forms.ModelMultipleChoiceField(queryset=User.objects.none(), widget=forms.CheckboxSelectMultiple(), required=True)
 #self.fields['UserStorys'] = forms.ChoiceField(choices=[ (o.id, str(o)) for o in Sprint.objects.filter(Proyecto_asignado=Proyecto_asignado)])       