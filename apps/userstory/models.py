from django.db import models
from apps.usuario.models import User
from apps.proyectos.models import Proyecto
from apps.flujos.models import Flujo, Actividad
import ast
from apps.archivos.models import Document

class ListField(models.TextField):
    __metaclass__ = models.SubfieldBase
    description = "Stores a python list"

    def __init__(self, *args, **kwargs):
        super(ListField, self).__init__(*args, **kwargs)

    def to_python(self, value):
        if not value:
            value = []

        if isinstance(value, list):
            return value

        return ast.literal_eval(value)

    def get_prep_value(self, value):
        if value is None:
            return value

        return unicode(value)

    def value_to_string(self, obj):
        value = self._get_val_from_obj(obj)
        return self.get_db_prep_value(value)


class UserStory(models.Model):
    """
    Clase Proyecto:
        * Contiene los campos de la tabla proyecto en la base de datos

        * Variales
            -   Scrum_Master: es el usuario lider del proyecto
            -   Nombre: es el nombre que posee el proyecto
            -   Descripcion: es la decripcion del proyecto
            -   Fecha de inicio: es la fecha en que el proyecto dara inicio
            -   Fecha de finalizacion: es la fecha en la que el proyecto estara finalizado
            -   Fecha: es la fecha de creacion del proyecto
    """
    Estados_US = (
        ('Pendiente', 'Pendiente'),
        ('AsignadoSprint','AsignadoSprint'),
        ('AsignadoFlujo','AsignadoFlujo'),
        ('AsignadoSprintActivo','AsignadoSprintActivo'),
        ('Resuelta','Resuelta'),
        ('Cancelado','Cancelado'),
        ('Terminado','Terminado'),
    )

    Prioridad_US=(
        ('Baja', 'Baja'),
        ('Normal', 'Normal'),
        ('Alta', 'Alta'),
    )

    Porcentaje_Realizado_US=(
        ('0%', '0%'),
        ('10%', '10%'),
        ('20%', '20%'),
        ('30%', '30%'),
        ('40%', '40%'),
        ('50%', '50%'),
        ('60%', '60%'),
        ('70%', '70%'),
        ('80%', '80%'),
        ('90%', '90%'),
        ('100%', '100%'),
    )
    
    Estados_actividad = (
        ('none', 'none'),
        ('to_do', 'to_do'),
        ('doing', 'doing'),
        ('done', 'done'),
    )

    Usuario_asignado = models.ForeignKey(User, null=True, related_name='Usuario_asignado')
    Nombre = models.CharField(max_length=30, unique=False)
    Descripcion = models.TextField(null=True)
    Valor_tecnico = models.PositiveIntegerField(null=True, blank=True)
    Valor_de_negocio = models.PositiveIntegerField(null=True, blank=True)
    Size = models.PositiveIntegerField(null=True, blank=True)
    Estado = models.CharField( max_length=30, choices=Estados_US, default='Pendiente', unique=False)
    is_active = models.BooleanField(default=True)
    Version = models.PositiveIntegerField(null=True, blank=True, default=0)
    Sub_version = models.PositiveIntegerField(null=True, blank=True, default=0)

    
    
    Usuario_creador = models.ForeignKey(User, null=True)
    Proyecto_asignado = models.ForeignKey (Proyecto, null=True)
    Fecha_creacion = models.DateTimeField(auto_now=True, null=True)

    in_kanban = models.BooleanField(default=False)
    Estado_de_actividad = models.CharField( max_length=30, choices=Estados_actividad, default='none', unique=False)
    Actividad_asignada = models.ForeignKey( Actividad, null=True )

    Prioridad = models.PositiveIntegerField(null=False, default=0)
    Bloqueado = models.BooleanField(default=False)

    Registro = ListField( null=True )
    Fecha_inicio = models.DateField('Fecha de inicio', blank=True, null=True)
    Fecha_finalizacion = models.DateField('Fecha de finalizacion', blank=True, null=True)
    Duracion = models.PositiveIntegerField(default=0)
    Restante = models.PositiveIntegerField(default = 0)
    
    class Meta:
        ordering = ['Nombre']
        permissions = (
                      ("avanzar_us", "puede avanzar el userstory"),
                      ("retroceder_us", "puede retroceder el userstory"),
                      ("asignar_horas_us", "puede asignar horas al userstory"),
                      ("cambiar_estado_us","cambiar estado del userstory"),
                      ("finalizar_us", "puede finalizar un userstory"),
        )

    def __str__(self):
        return self.Nombre 

    def get_tabla(self):

        if (self.in_kanban):
            return Flujo.objects.get( pk=self.Actividad_asignada.idTabla ).Nombre
        else:
            return 'none'

    def get_sprint(self):

        sprints = self.sprint.filter(Estado = 'En_curso')

        for s in sprints.all():
            return s

        

class CargarHoras(models.Model):
    Horas = models.PositiveIntegerField(null=True, blank=True, default=0)
    Descripcion = models.TextField(null=True)
    US_asignado= models.ForeignKey(UserStory, null=True)
    Archivos_adjuntos = models.ManyToManyField(Document, null=True, related_name='archivos_adjuntos')