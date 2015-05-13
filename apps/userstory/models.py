from django.db import models
from apps.usuario.models import User
from apps.proyectos.models import Proyecto
from apps.flujos.models import Flujo, Actividad

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

    
class CargarHoras(models.Model):
    Horas = models.PositiveIntegerField(null=True, blank=True, default=0)
    Descripcion = models.TextField(null=True)
    US_asignado= models.ForeignKey(UserStory, null=True)