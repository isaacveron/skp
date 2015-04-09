from django.db import models
from django.contrib.auth.models import Group,User, Permission
from django.contrib.contenttypes.models import ContentType

# Create your models here.
Group.add_to_class('Usuario', models.ForeignKey(User, null=True))
Group.add_to_class('Fecha', models.DateTimeField(auto_now=True, null=True))
