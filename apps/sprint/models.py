from django.db import models
from apps.usuario.models import User
from apps.userstory.models import UserStory
from apps.proyectos.models import Proyecto
from apps.flujos.models import Flujo, Actividad
# Create your models here.
class Sprint(models.Model):
    """
    Clase Sprint:
        * Contiene los campos de la tabla sprint en la base de datos

        * Variales
            -   Scrum_Master: es el usuario lider del proyecto
            -   Nombre: es el nombre que posee el proyecto
            -   Descripcion: es la decripcion del proyecto
            -   Fecha de inicio: es la fecha en que el proyecto dara inicio
            -   Fecha de finalizacion: es la fecha en la que el proyecto estara finalizado
            -   Fecha: es la fecha de creacion del proyecto
    """   
    Estados_sprint = (
        ('Pendiente','Pendiente'),
        ('En_curso','En_curso'),
        ('Terminado','Terminado'),
        ('Cancelado','Cancelado'),        
    )

    Nombre = models.CharField(max_length=30, unique=True)
    Descripcion = models.TextField(null=True)
    Fecha_inicio = models.DateField('Fecha de inicio', blank=True, null=True)
    Fecha_finalizacion = models.DateField('Fecha de finalizacion', blank=True, null=True)
    Duracion = models.PositiveIntegerField(null=True, blank=True)
    Cliente = models.CharField( max_length=30 , blank=True, null=True)
    is_active = models.BooleanField(default=True)
    Estado = models.CharField( max_length=30, choices=Estados_sprint, default='Pendiente', unique=False)
    UserStorys = models.ManyToManyField(UserStory, null=True, related_name='UserStorys')
    Usuario_creador = models.ForeignKey(User, null=True)
    Proyecto_asignado = models.ForeignKey (Proyecto, null=True)
    Fecha_creacion = models.DateTimeField(auto_now=True, null=True)
    Tabla_asignada = models.ForeignKey(Flujo, null=True)

    def __str__(self):              
        return self.Nombre

    class Meta:
        permissions = (
                      ("iniciar_sprint", "puede iniciar el sprint"),
                      ("detener_sprint", "puede detener el sprint"),
                      ("cambiar_estado_sprint", "puede cambiar el estado del sprint"),
        )
