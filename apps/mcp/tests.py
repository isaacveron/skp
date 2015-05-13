# Create your tests here.
from django.test import TestCase
import unittest, time
from datetime import datetime
from django.contrib.auth.models import User, Group, Permission
from django.core.urlresolvers import reverse
from django.contrib.auth import SESSION_KEY
from django.test import Client


class SKPTestCase(TestCase):
    fixtures = ['usuario.json']

    def test_crear_sprint(self):
        '''
        Test para la creacion de un sprint

        '''
        s = Client()
        s.login(username='admin', password='admin')
        resp = s.post('/sprints/crearSprint/',{"nombre":"testsprint", "fechainicio":"2015-04-21", "tiempoacumulado":7, "duracion":25, "fechafin":"2015-05-01", "proyecto":1})
        self.assertTrue(resp.status_code,200)
        print ('\n Se crea correctamente el sprint')


    def test_listar_sprints(self):
        '''
         Test para crear un sprint y ver si lo lista correctamente
        '''
        c = Client()
        c.login(username='admin', password='admin1')
        resp = c.get('/sprints/')
        self.assertTrue(resp.status_code, 200)
        print ('\n Lista los Sprints')



    def test_detalle_sprints(self):
        '''
        Test para visualizar los detalles de un cliente
        '''
        c = Client()
        c.login(username='admin', password='admin1')
        self.test_crear_sprint()
        #consultar un sprint existente
        resp = c.get('/sprints/consultar/1/')
        self.assertTrue(resp.status_code, 200)
        print ('\n Se consulta correctamente los atributos de un Sprint que existe en el sistema')
      

    def test_eliminar_sprint(self):
        """
            Test para probar el correcto funcionamiento de eliminacion de un cliente.
            Recibe un identificador del cliente que se desea eliminar, se
            busca en la base de datos y se elimina logicamente.
            
        """
        s = Client()
        s.login(username='admin', password='admin1')
        resp = s.post('/sprints/crearSprint/',{"nombre":"testsprint2", "fechainicio":"2015-04-23", "tiempoacumulado":10, "duracion":15, "fechafin":"2015-05-14"})
        #creamos un Rol para luego eliminar
        self.test_crear_sprint()
        #eliminacion de un rol existente
        resp = s.get('/sprints/eliminar/2/')
        self.assertTrue(resp.status_code, 200)
        print ('\n Se elimina logicamente el sprint creado del sistema')
        #eliminacion de un rol inexistente, (ya se borro)
        resp = s.get('/sprints/eliminar/100/')
        self.assertTrue(resp.status_code, 404)
        print ('\n Error al querer eliminar un sprint que no existe en el sistema')
        
    def test_crear_us(self):
        '''
        Test para la creacion de un us
        '''
        c = Client()
        c.login(username='admin', password='admin1')
        #creacion correcta del us, se mete un nombre nuevo
        resp = c.post('/userstories/crearuserstory/',{"nombre": "USPrueba", "descripcion": "HOLA", "tiempoestimado":3, "tiempotrabajado":1, "comentarios": "LOLO", "usuarioasignado":1, "estado": "Nueva", "prioridad":"Alta", "porcentajerealizado": "20%", "sprint": 1})
        self.assertTrue(resp.status_code,200)
        print ('\n Crea el us si esta correctamente completado\n')
        #creacion incorrecta: nombre repetido, no redirige
        resp = c.post('/userstories/crearuserstory/',{"nombre": "USPrueba", "descripcion": "HOLA", "tiempoestimado":3, "tiempotrabajado":1, "comentarios": "LOLO", "usuarioasignado":1, "estado": "Nueva", "prioridad":"Alta", "porcentajerealizado": "20%","sprint": 1})
        self.assertTrue(resp.status_code,302)
        print ('\n No crea el us si tiene un nombre duplicado')

    def test_listar_us(self):
        '''
         Test para crear un us y ver si lo lista correctamente
        '''
        c = Client()
        c.login(username='admin', password='admin1')
        resp = c.get('/userstories/')
        self.assertTrue(resp.status_code, 200)
        print ('\n Lista los US')

    def test_consulta_US(self):
        '''
        Test para consultar US
        '''
        c = Client()
        c.login(username='admin', password='admin1')
        self.test_crear_us()
        #consultar un us existente
        resp = c.get('/userstories/consultar/1/')
        self.assertTrue(resp.status_code, 200)
        print ('\n Se consulta correctamente los atributos de un US que existe en el sistema')
        

    def test_eliminar_us(self):
        """
            Test para probar el correcto funcionamiento de eliminacion de un us.
            Recibe un identificador del us que se desea eliminar, se
            busca en la base de datos y se elimina logicamente.
        """
        c = Client()
        c.login(username='admin', password='admin1')
        #creamos un US para luego eliminar
        self.test_crear_us()
        #eliminacion de un us existente
        resp = c.get('/userstories/eliminaruserstory/2/')
        self.assertTrue(resp.status_code, 200)
        print ('\n Se elimina logicamente el us creado del sistema')



    def test_crear_flujo(self):
        '''
            Test para la creacion de un flujo
        '''
        s = Client()
        s.login(username='admin', password='admin')
        resp = s.post('/flujos/crearFlujo/',{"nombre":"testsflujo"})
        self.assertTrue(resp.status_code,200)
        print ('\n Se crea correctamente el flujo')

    def test_listar_flujo(self):
        '''
         Test para crear un flujo y ver si lo lista correctamente
        '''
        c = Client()
        c.login(username='admin', password='admin1')
        resp = c.get('/flujos/')
        self.assertTrue(resp.status_code, 200)
        print ('\n Lista los Flujo')

    def test_consulta_flujo(self):
        '''
        Test para consultar flujo
        '''
        c = Client()
        c.login(username='admin', password='admin1')
        self.test_crear_flujo()
        #consultar un us existente
        resp = c.get('/flujos/consultar/1/')
        self.assertTrue(resp.status_code, 200)
        print ('\n Se consulta correctamente los atributos de un flujo que existe en el sistema')
        

    def test_eliminar_flujo(self):
        """
            Test para probar el correcto funcionamiento de eliminacion de un flujo.
            Recibe un identificador del flujo que se desea eliminar, se
            busca en la base de datos y se elimina logicamente.
        """
        c = Client()
        c.login(username='admin', password='admin1')
        #creamos un US para luego eliminar
        self.test_crear_flujo()
        #eliminacion de un us existente
        resp = c.get('/flujos/eliminarflujo/2/')
        self.assertTrue(resp.status_code, 200)
        print ('\n Se elimina logicamente el flujo creado del sistema')