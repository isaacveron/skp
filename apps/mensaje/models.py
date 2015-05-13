from django.db import models
from apps.roles.models import User

# Create your models here.
class Mensaje(models.Model):
	Usuario_a_enviar = models.ForeignKey(User, null=True, related_name='Usuario_a_enviar')
	Contenido_mensaje= models.TextField(null=True, blank=True)
	Usuario_que_envio = models.ForeignKey(User, null=True, related_name='Usuario_que_envio')

