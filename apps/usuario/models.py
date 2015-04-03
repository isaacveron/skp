from django.db import models
from django.contrib.auth.models import User, Permission
from django.contrib.contenttypes.models import ContentType

"""
Se utiliza la clase User por de defecto en Django para la creacion de los usuarios, pero se incluyen 3 atributos:
    - direccion: direccion del usuario
    - telefono: numero del telefono del usuario
    - observacion: observacion sobre el usuario por parte del administrador del sistema
"""
# Create your models here.
User.add_to_class('direccion', models.TextField(null=True, blank=True))
User.add_to_class('telefono', models.PositiveIntegerField(null=True, blank=True))
User.add_to_class('observacion', models.TextField(null=True, blank=True))
