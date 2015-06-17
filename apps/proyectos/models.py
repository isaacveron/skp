from django.db import models
from apps.roles.models import Group
from apps.usuario.models import User
from apps.flujos.models import Flujo
from datetime import datetime, timedelta
import ast

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

class Proyecto(models.Model):
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

    Estados_P = (
        ('Pendiente', 'Pendiente'),
        ('Activo','Activo'),
        ('Terminado','Terminado'),
        ('Cancelado','Cancelado'),
    )

    Scrum_Master = models.ForeignKey(User, null=True, related_name='Scrum_Master')
    Grupo_trabajo = models.ManyToManyField(User, null=True, related_name='Proyectos')
    Nombre = models.CharField(max_length=30, unique=True)
    Descripcion = models.TextField(null=True, blank=True)
    Cliente = models.CharField( max_length=30 , blank=True, null=True)
    Estado = models.CharField( max_length=30, choices=Estados_P, default='Activo', unique=False)
    
    Estado = models.CharField( max_length=15, default='Pendiente', unique=False)
    Usuario_creador = models.ForeignKey(User, null=True)
    Fecha_creacion = models.DateTimeField(auto_now=True, null=True)
    Tablas = models.ManyToManyField(Flujo, null=True)

    Dia_actual = models.DateField(default = datetime.now())
    sprint_activo = models.BooleanField(default=False)

    Registro = ListField( null=True )
    Duracion = models.PositiveIntegerField(default=0)
    Restante = models.PositiveIntegerField(default = 0)
    Fecha_inicio = models.DateField('Fecha de inicio', null=True, blank = False)
    Fecha_finalizacion = models.DateField('Fecha de finalizacion', blank=False, null=True)

    def __str__(self):
        return self.Nombre

    class Meta:
        ordering = ['Nombre']



