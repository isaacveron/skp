from django.db import models
from apps.roles.models import Group
from apps.usuario.models import User
from apps.proyectos.models import Proyecto

# Create your models here.

class Actividad(models.Model):
	Nombre = models.CharField(max_length=30)
	Orden = models.IntegerField(null=True)
	idTabla = models.IntegerField(null=True)
	#To_do = models.ManyToManyField(UserStory)
	#Doing = models.ManyToManyField(UserStory)
	#Done = models.ManyToManyField(UserStory)
	
	def __str__(self):
		return self.Nombre



class Flujo(models.Model):

	Nombre = models.CharField(max_length=30, unique=True)
	Usuario_creador = models.ForeignKey(User, null=True)
	Estado = models.CharField( max_length=15, default='Activo', unique=False)
	Descripcion = models.TextField(null=True, blank=True)
	Fecha_creacion = models.DateTimeField(auto_now=True, null=True)
	Actividades = models.ManyToManyField(Actividad, null=True)

	def __str__(self):
		return self.Nombre





