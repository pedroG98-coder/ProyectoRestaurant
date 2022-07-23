from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status


from appSecond.models import Cliente



class ClienteTestCase(TestCase):
    def setUp(self): #INICIALIZADOR
        cliente = Cliente(
            nombre = 'testing_login@cosasdedevs.com',
            apellidos = '',
            calle = '',
            ciudad = '',
            email = '',
            cp = '',
            telefono = ''
        )
        cliente.save()
        
       