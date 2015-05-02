from django.db import models
from apps.roles.models import Group
from apps.usuario.models import User
from apps.flujos.models import Flujo

# Create your models here.
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
    Scrum_Master = models.ForeignKey(User, null=True, related_name='Scrum_Master')
    Grupo_trabajo = models.ManyToManyField(User, null=True, related_name='Proyectos')
    Nombre = models.CharField(max_length=30, unique=True)
    Descripcion = models.TextField(null=True, blank=True)
    Fecha_inicio = models.DateField('Fecha de inicio', blank=True, null=True)
    Fecha_finalizacion = models.DateField('Fecha de finalizacion', blank=True, null=True)
    Cliente = models.CharField( max_length=30 , blank=True, null=True)
    Estado = models.CharField( max_length=15, default='Pendiente', unique=False)
    Usuario_creador = models.ForeignKey(User, null=True)
    Fecha_creacion = models.DateTimeField(auto_now=True, null=True)
    Tablas = models.ManyToManyField(Flujo, null=True)

    def __str__(self):
        return self.Nombre

    class Meta:
        ordering = ['Nombre']