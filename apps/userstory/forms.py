from django.forms import ModelForm, SelectMultiple

from apps.roles.models import User, Group
from apps.userstory.models import UserStory, CargarHoras
from apps.proyectos.models import Proyecto

Estados_US = (
    ('AsignadoSprint','AsignadoSprint'),
    ('AsignadoSprintActivo','AsignadoSprintActivo'),
    ('AsignadoFlujo','AsignadoFlujo'),
    ('Resuelta','Resuelta'),
    ('Cancelado','Cancelado'),
)

class UserStoryForm(ModelForm):
    
    
    def __init__(self, idProyecto, *args, **kwargs):
        super(UserStoryForm, self).__init__(*args, **kwargs)
        self.fields['Usuario_asignado'].queryset = User.objects.filter(Proyectos__id=idProyecto)
    class Meta:
        model = UserStory 
        exclude = ['Version','Sub_version','in_kanban','Actividad_asignada','Estado_de_actividad','actividad_asignada','estado_actividad','is_active', 'Proyecto_asignado', 'Usuario_creador','Estado' , 'Usuario_creador' , 'Fecha_creacion']

class UserStoryFormMod(ModelForm):
    """
    Formulario para el la creacion de roles
    Hereda de forms.ModelForm y utiliza la clase Group para
    """
    
    def __init__(self, *args, **kwargs):
        super(UserStoryFormMod, self).__init__(*args, **kwargs)
        self.fields['Usuario_asignado'].queryset = User.objects.filter(Proyectos__id=self.instance.Proyecto_asignado.id)
    class Meta:
        model = UserStory 
        exclude = ['Version','Sub_version','in_kanban','Actividad_asignada','Estado_de_actividad','actividad_asignada','estado_actividad','is_active', 'Proyecto_asignado', 'Usuario_creador','Estado' , 'Usuario_creador' , 'Fecha_creacion']


class UserStoryFormDelete(ModelForm):    
    class Meta:
        model = UserStory
        fields=('is_active',)

class CargarHorasForm(ModelForm):
    class Meta:
        model = CargarHoras
        fields=('Horas', 'Descripcion') 
            
        