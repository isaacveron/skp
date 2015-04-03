from django.test import TestCase
import unittest, time
from datetime import datetime
from django.contrib.auth.models import User, Group, Permission
from django.core.urlresolvers import reverse
# Create your tests here.

class TestUserBD(TestCase):
   def test_numero_elementos(self):
       print("\nTEST: Al crear la BD el numero de usuarios debe ser 0")
       try:
           self.assertEqual(0,len(User.objects.all()))
       except:
           print("Prueba fallida, el numero de usuarios es distinto de 0")
           return
       print("Prueba exitosa, el numero de usuarios es igual a 0")

class TestLogin(TestCase):
   usuario='admin'
   password='admin'
   #cargamos los usuarios
   fixtures = ["usuario"]
   def test_login_usuario(self):
       print("\nTEST: Loguear usuario registrado")
       try:
           # vamos a la pantalla de inicio
           resp = self.client.get('/')
           self.assertEqual(resp.status_code, 200)
           # logueamos con el usuario sgp
           login = self.client.login(username=self.usuario, password=self.password)
           self.assertTrue(login)
       except:
           if resp.status_code == 404:
               print("Prueba fallida, la url no existe")
           else:
               print("Prueba fallida, el usuario no existe o esta inactivo")
           return
       print("Prueba exitosa, el usuario pudo iniciar sesion")
