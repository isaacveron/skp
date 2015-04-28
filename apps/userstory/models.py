from django.db import models
from apps.usuario.models import User
from apps.proyectos.models import Proyecto

# Create your models here.
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
    
    Usuario_asignado = models.ForeignKey(User, null=True, related_name='Usuario_asignado')
    Nombre = models.CharField(max_length=30, unique=True)
    Descripcion = models.TextField(null=True)
    Valor_tecnico = models.PositiveIntegerField(null=True, blank=True)
    Valor_de_negocio = models.PositiveIntegerField(null=True, blank=True)
    Size = models.PositiveIntegerField(null=True, blank=True)
    Estado = models.CharField( max_length=15, default='Pendiente', unique=False)
    is_active = models.BooleanField(default=True)
    Usuario_creador = models.ForeignKey(User, null=True)
    Proyecto_asignado = models.ForeignKey (Proyecto, null=True)
    Fecha_creacion = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):              
        return self.Nombre