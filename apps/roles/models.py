from django.db import models
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from apps.usuario.models import User

# Create your models here.
#Group.add_to_class('Usuario', models.ForeignKey(User, null=True))
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

def can_delete_proyecto(self):
    permiso = 'delete_proyecto'
    return self.tienePermiso(permiso)

def can_change_proyecto(self):
    permiso = 'change_proyecto'
    return self.tienePermiso(permiso)

def can_add_flujo(self):
    permiso = 'add_flujo'
    return self.tienePermiso(permiso)

def can_delete_flujo(self):
    permiso = 'delete_flujo'
    return self.tienePermiso(permiso)

def can_change_flujo(self):
    permiso = 'change_flujo'
    return self.tienePermiso(permiso)

User.add_to_class('can_add_proyecto', can_add_proyecto)
User.add_to_class('can_change_proyecto', can_change_proyecto)
User.add_to_class('can_delete_proyecto', can_delete_proyecto)
User.add_to_class('can_add_flujo', can_add_flujo)
User.add_to_class('can_change_flujo', can_change_flujo)
User.add_to_class('can_delete_flujo', can_delete_flujo)
