from django.test import TestCase
from apps.flujos.models import Flujo, Actividad
from django.test.client import RequestFactory
from apps.roles.models import Group
from apps.usuario.models import User
from apps.proyectos.models import Proyecto
from django.test import Client
import unittest, time
from datetime import datetime
from django.core.urlresolvers import reverse
from django.contrib.auth import SESSION_KEY



# Create your tests here.

class TestFlujos(TestCase):
	fixtures = ['usuario.json']


	def test_crear_tabla_kanban(self):

		tabla = Flujo(Nombre='flujo_prueba', Estado = 'activo', Descripcion = 'AAAAAAAAA')
		tabla.save()

		actividad_1 = Actividad(Nombre = 'actividad 1', Orden = 1, idTabla = tabla.id)
		actividad_1.save()
		actividad_2 = Actividad(Nombre = 'actividad 2', Orden = 2, idTabla = tabla.id)
		actividad_2.save()
		actividad_3 = Actividad(Nombre = 'actividad 3', Orden = 3, idTabla = tabla.id)
		actividad_3.save()

		tabla.Actividades.add(actividad_1)
		tabla.Actividades.add(actividad_2)
		tabla.Actividades.add(actividad_3)
		tabla.save()

		tabla_prueba = Flujo.objects.get(Nombre='flujo_prueba')
		
		# Comprueba si se creo la tabla correcatamente
		self.assertTrue( len(Flujo.objects.all())  == 1)

		# Comprueba que las actividades se crearon y agregaron correcatamente
		self.assertTrue( len( tabla_prueba.Actividades.all() ) == 3 )
		actividad_prueba = tabla_prueba.Actividades.get(Nombre = 'actividad 1')
		self.assertTrue( actividad_prueba.Orden == 1 )
		actividad_prueba = tabla_prueba.Actividades.get(Nombre = 'actividad 2')
		self.assertTrue( actividad_prueba.Orden == 2 )
		actividad_prueba = tabla_prueba.Actividades.get(Nombre = 'actividad 3')
		self.assertTrue( actividad_prueba.Orden == 3 )


	def test_eliminar_tabla_kanban(self):
		tabla = Flujo(Nombre='flujo_prueba', Estado = 'activo', Descripcion = 'AAAAAAAAA')
		tabla.save()

		# Comprueba si se creo la tabla correcatamente
		self.assertTrue( len( Flujo.objects.all() ) == 1 )


		tabla_prueba = Flujo.objects.get(Nombre='flujo_prueba')
		tabla_prueba.delete()

		self.assertTrue( len( Flujo.objects.all() ) == 0 )

	def test_modificar_tabla_kanban(self):
		tabla = Flujo(Nombre='flujo_prueba', Estado = 'activo', Descripcion = 'AAAAAAAAA')
		tabla.save()


		# Comprueba si se creo la tabla correcatamente
		self.assertTrue( len( Flujo.objects.all() ) == 1 )

		tabla = Flujo.objects.get(Nombre = 'flujo_prueba')

		tabla.Nombre = 'nombre_modificado'
		tabla.save()

		tabla = Flujo.objects.get(Nombre = 'nombre_modificado')
		self.assertTrue( tabla.Nombre == 'nombre_modificado' )


	




		










