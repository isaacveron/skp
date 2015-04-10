from django.db.models import 
from django.test import Client
from django.test import TestCase
from django.contrib.auth.models import User, Group

class TestCase(TestCase):

    fixtures = ["usuarios"]

    username = 'admin'
    password = 'admin'

    def test_loguin_admin(self):
        """ Test para loguear al administrador. """
        
        resp = self.client.get('/login/')                                           #Solicitud de la pagina de autenticacion
        self.assertEqual(resp.status_code, 200)                                     #Pagina de login recibida con exito
        login = self.client.login(username=self.username, password=self.password)   #Proceso de autenticacion
        logout= self.client.logout()                                                #Cerramos la sesion actual
        self.assertFalse(logout)                                                    #Probamos que efectivamente la sesion esta cerrada
        resp = self.client.get('/index/')                                           #Pasamos a la pagina de inicio
        self.assertNotEqual(resp.status_code, 200)                                  #Probamos que ya no podemos acceder al sistema si no estamos logueados
        print 'Test de login administrador ejecutado exitosamente.'
    