from django.test import TestCase
import unittest, time
from datetime import datetime
from django.test.client import RequestFactory
from django.contrib.auth.models import Permission
from apps.roles.models import Group
from apps.usuario.models import User
from apps.proyectos.models import Proyecto
from django.core.urlresolvers import reverse

# Create your tests here.
class TestCrearModelo(TestCase):
    fixtures = ['usuario.json']

    def setUp(self):
        """ Inicializamos la variable factory que posteriormente nos permitira cargar
            un request para utilizarlo en las visata.
        """
        self.factory = RequestFactory()
        

    def test_crear_usuario(self):
        print("\nTEST: Crear usuario")
        nombre_usuario ='prueba'
        password_usuario ='prueba'
        try:
            user = User(username=nombre_usuario, password=password_usuario)
            user.save()
        except:
            print("Prueba fallida, no se pudo crear el usuario")
            return
        if len(User.objects.all()) == 2:
            print("Prueba exitosa, el usuario fue creado correctamente")
        else:
            print("Prueba fallida, no se pudo crear el usuario")

    def test_crear_rol(self):
        print("\nTEST: Crear rol")
        nombre_rol ='prueba'
        try:
            rol = Group(name=nombre_rol)
            rol.save()
        except:
            print("Prueba fallida, no se pudo crear el rol")
            return
        if len(Group.objects.all()) == 1:
            print("Prueba exitosa, el rol fue creado correctamente")
        else:
            print("Prueba fallida, no se pudo crear el rol")
        

    def test_crear_proyecto(self):
        print("\nTEST: Crear proyecto")
        nombre_proyecto ='prueba'
        userPk = '1'
        usuario = User.objects.get(pk=userPk)
        Descripcion = "proyecto prueba"
        Fecha_inicio = datetime.now()
        Fecha_finalizacion = datetime.now()

        try:
            proyecto = Proyecto(Nombre=nombre_proyecto,Scrum_Master=usuario,Descripcion=Descripcion,
                                Fecha_inicio=Fecha_inicio,Fecha_finalizacion=Fecha_finalizacion)
            proyecto.save()
        except:
            print("Prueba fallida, no se pudo crear el proyecto2")
            return
        if len(Proyecto.objects.all()) == 1:
            print("Prueba exitosa, el proyecto fue creado correctamente")
        else:
            print("Prueba fallida, no se pudo crear el proyecto")























































            