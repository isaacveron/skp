from django.db import models
from apps.roles.models import Group
from apps.usuario.models import User
from apps import userstory

# Create your models here.

class Actividad(models.Model):
	Nombre = models.CharField(max_length=30)
	Orden = models.IntegerField(null=True)
	idTabla = models.IntegerField(null=True)
	To_do = models.ManyToManyField('userstory.UserStory', null=True, related_name='To_do')
	Doing = models.ManyToManyField('userstory.UserStory', null=True, related_name='Doing')
	Done = models.ManyToManyField('userstory.UserStory', null=True, related_name='Done')
	def __str__(self):
		return self.Nombre

	class Meta:
		ordering = ['Orden',]


class Flujo(models.Model):

	Nombre = models.CharField(max_length=30, unique=False)
	Usuario_creador = models.ForeignKey(User, null=True)
	Estado = models.CharField( max_length=15, default='Activo', unique=False)
	Descripcion = models.TextField(null=True, blank=True)
	Fecha_creacion = models.DateTimeField(auto_now=True, null=True)
	Actividades = models.ManyToManyField(Actividad, null=True)
	Copia = models.BooleanField(default=False)
	
	def __str__(self):
		return self.Nombre



	def agregar_us(self, us):
		self.Actividades.get(Orden=1).To_do.add(us)


	





