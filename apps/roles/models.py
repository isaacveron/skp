from django.db import models
from django.contrib.auth.models import Group,User, Permission
from django.contrib.contenttypes.models import ContentType

# Create your models here.
Group.add_to_class('Usuario', models.ForeignKey(User, null=True))
Group.add_to_class('Fecha', models.DateTimeField(auto_now=True, null=True))


def tienePermiso(self, permiso):
    for grupo in self.groups.all():
        for permisoUsuario in grupo.permissions.all():
            if permisoUsuario.codename == permiso:
                return True
    return False

User.add_to_class('tienePermiso', tienePermiso)


def can_add_proyecto(self):
    permiso = 'add_proyecto'
    return self.tienePermiso(permiso)
User.add_to_class('can_add_proyecto', can_add_proyecto)
