from django.test import TestCase
from appSecond.helpers_Reportes import consulta_mesas_con_mas_de_cin_personas, consulta_mesas_por_num_personas, consulta_pedidos_por_cliente, consulta_pedidos_por_mesa, consulta_pedidos_por_mesero, consulta_top_clientes, consulta_top_platillos
from appSecond.test_factoryAppSecond import cliente_factory, factura_factory, mesa_factory, mesero_factory, pedido_factory, platillo_factory
from rest_framework.test import force_authenticate, APITestCase, APIClient
from appSecond import models,helpers_Reportes,serializers
from django.contrib.auth.models import User
from rest_framework import status
from appSecond import test_factoryAppSecond
from django.db.models import Count


#CLASE TEST_CLIENTE
class test_clienteLista(TestCase):
    
        #POST CLIENTE
    def test_post_required_ClienteLista(self):
        myuser = User.objects.create_user('username', 'example@gmail.com', 'youPassword')
        myuser.save()
        self.client = APIClient()
        self.client.force_authenticate(myuser)
        data = {
            "nombre": "Felipe",
            "apellido_paterno": "Garcia",
            "apellido_materno": "Cortes",
            "calle": "Juan Enriquez",
            "ciudad": "Veracruz",
            "email": "felipe.18@gmail.com",
            "cp": "93100",
            "telefono": "7841256598",
        }
        response = self.client.post( '/app-second/cliente',data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)    
        
        #GET CLIENTE
    def test_get_required_ClienteDetalle(self):
        myuser = User.objects.create_user('username', 'example@gmail.com', 'youPassword')
        myuser.save()
        self.client = APIClient()
        self.client.force_authenticate(myuser)
        cliente = cliente_factory()
        response = self.client.get( '/app-second/cliente/1')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEquals(cliente.nombre, (cliente.nombre))
        
        #DELETE_CLIENTE
    def test_delete_required_ClienteDetalle(self):
        myuser = User.objects.create_user('username', 'example@gmail.com', 'youPassword')
        myuser.save()
        self.client = APIClient()
        self.client.force_authenticate(myuser)
        cliente = cliente_factory()
        response = self.client.delete( '/app-second/cliente/1')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEquals(cliente.id, (cliente.id))
    
        #PUT_CLIENTE
    def test_put_required_ClienteDetalle(self):
        cliente = cliente_factory()
        myuser = User.objects.create_user('username', 'example@gmail.com', 'youPassword')
        myuser.save()
        self.client = APIClient()
        self.client.force_authenticate(myuser)
        data = {
            "nombre": "Andres",
            "apellido_paterno": "Garcia",
            "apellido_materno": "Cortes",
            "calle": "Juan Enriquez",
            "ciudad": "Veracruz",
            "email": "felipe.18@gmail.com",
            "cp": "93100",
            "telefono": "7841256598"
        }
        response = self.client.put( '/app-second/cliente/1',data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEquals(cliente.nombre, (cliente.nombre))
        
#CLASE TEST_MESA     
class test_mesaLista(TestCase):
    
        #POST_MESA
    def test_post_required_MesaLista(self):
        cliente = cliente_factory()
        pedido = pedido_factory()
        #print(cliente.id)
        myuser = User.objects.create_user('username', 'example@gmail.com', 'youPassword')
        myuser.save()
        self.client = APIClient()
        self.client.force_authenticate(myuser)
        data = {
            "num_personas": 6,
            "id_cliente": 1,
            "id_pedido": [1] 
        }
        response = self.client.post( '/app-second/mesa',data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEquals(cliente.nombre, (cliente.nombre))
        self.assertEquals(pedido.id, (pedido.id))
        
        #GET_MESA
    def test_get_required_MesaDetalle(self):
        cliente = cliente_factory()
        mesa = mesa_factory()
        myuser = User.objects.create_user('username', 'example@gmail.com', 'youPassword')
        myuser.save()
        self.client = APIClient()
        self.client.force_authenticate(myuser)
        response = self.client.get( '/app-second/mesa/1')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEquals(cliente.nombre, (cliente.nombre))
        self.assertEquals(mesa.num_personas, (mesa.num_personas))
        
        #DELETE_MESA
    def test_delete_required_MesaDetalle(self):
        myuser = User.objects.create_user('username', 'example@gmail.com', 'youPassword')
        myuser.save()
        self.client = APIClient()
        self.client.force_authenticate(myuser)
        mesa = mesa_factory()
        response = self.client.delete( '/app-second/mesa/1')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEquals(mesa.num_personas, (mesa.num_personas))
            
        #PUT_MESA
    def test_put_required_MesaDetalle(self):
        mesa = mesa_factory()
        pedido = pedido_factory()
        myuser = User.objects.create_user('username', 'example@gmail.com', 'youPassword')
        myuser.save()
        self.client = APIClient()
        self.client.force_authenticate(myuser)
        data = {
            "num_personas": 5,
            "id_cliente": 1,
            "id_pedido": [1]
        }
        response = self.client.put( '/app-second/mesa/1',data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEquals(mesa.num_personas, (mesa.num_personas))
        self.assertEquals(pedido.id, (pedido.id))

##CLASE TEST_PEDIDO
class test_pedidoLista(TestCase):
    
        #POST_PEDIDO
    def test_post_required_PedidoLista(self):
        cliente = cliente_factory()
        #print(cliente.id)
        myuser = User.objects.create_user('username', 'example@gmail.com', 'youPassword')
        myuser.save()
        self.client = APIClient()
        self.client.force_authenticate(myuser)
        data = {
            "cant_pedidos": 4,
            "id_cliente": [1]  
        }
        response = self.client.post( '/app-second/pedido',data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEquals(cliente.nombre, (cliente.nombre))
        
        #GET_PEDIDO
    def test_get_required_PedidoDetalle(self):
        cliente = cliente_factory()
        pedido = pedido_factory()
        myuser = User.objects.create_user('username', 'example@gmail.com', 'youPassword')
        myuser.save()
        self.client = APIClient()
        self.client.force_authenticate(myuser)
        response = self.client.get( '/app-second/pedido/1')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEquals(cliente.nombre, (cliente.nombre))
        self.assertEquals(pedido.id, (pedido.id))
    
        #DELETE_PEDIDO
    def test_delete_required_PedidoDetalle(self):
        myuser = User.objects.create_user('username', 'example@gmail.com', 'youPassword')
        myuser.save()
        self.client = APIClient()
        self.client.force_authenticate(myuser)
        pedido = pedido_factory()
        response = self.client.delete( '/app-second/pedido/1')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEquals(pedido.id, (pedido.id))
        
        #PUT_PEDIDO
    def test_put_required_PedidoDetalle(self):
        cliente = cliente_factory()
        pedido = pedido_factory()
        myuser = User.objects.create_user('username', 'example@gmail.com', 'youPassword')
        myuser.save()
        self.client = APIClient()
        self.client.force_authenticate(myuser)
        data = {
            "cant_pedidos": 4,
            "id_cliente": [1] 
        }
        response = self.client.put( '/app-second/pedido/1',data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEquals(cliente.nombre, (cliente.nombre))
        self.assertEquals(pedido.id, (pedido.id))
        

#CLASE TEST_PLATILLO
class test_platilloLista(TestCase):
    
        #POST_PLATILLO
    def test_post_required_PlatilloLista(self):
        pedido = pedido_factory()
        myuser = User.objects.create_user('username', 'example@gmail.com', 'youPassword')
        myuser.save()
        self.client = APIClient()
        self.client.force_authenticate(myuser)
        data = {
            "nombre_platillo": "Milanesa de Res",
            "precio_platillo": 120,
            "bebida": "Coca Cola",
            "precio_bebida": 25,
            "id_pedido": [1], 
            "descripcion": "Milanesa de res con espaguetti y frijoles"
        }
        response = self.client.post( '/app-second/platillo',data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEquals(pedido.id, (pedido.id))
        
        #GET_PLATILLO
    def test_get_required_PlatilloDetalle(self):
        pedido = pedido_factory()
        platillo = platillo_factory()
        myuser = User.objects.create_user('username', 'example@gmail.com', 'youPassword')
        myuser.save()
        self.client = APIClient()
        self.client.force_authenticate(myuser)
        response = self.client.get( '/app-second/platillo/1')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEquals(pedido.id, (pedido.id))
        self.assertEquals(platillo.nombre_platillo, (platillo.nombre_platillo))
        
        #DELETE_PLATILLO
    def test_delete_required_PlatilloDetalle(self):
        myuser = User.objects.create_user('username', 'example@gmail.com', 'youPassword')
        myuser.save()
        self.client = APIClient()
        self.client.force_authenticate(myuser)
        platillo = platillo_factory()
        response = self.client.delete( '/app-second/platillo/1')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEquals(platillo.nombre_platillo, (platillo.nombre_platillo))
    
    #PUT PLATILLO
    def test_put_required_PlatilloDetalle(self):
        pedido = pedido_factory()
        platillo = platillo_factory()
        myuser = User.objects.create_user('username', 'example@gmail.com', 'youPassword')
        myuser.save()
        self.client = APIClient()
        self.client.force_authenticate(myuser)
        data = {
            "nombre_platillo": "Camarones en chiltepin",
            "precio_platillo": 180,
            "bebida": "Coca Cola",
            "precio_bebida": 25,
            "id_pedido": [1], 
            "descripcion": "Camarones en chiltepin con espaguetti y frijoles"
        }
        response = self.client.put( '/app-second/platillo/1',data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEquals(pedido.id, (pedido.id))
        self.assertEquals(platillo.nombre_platillo, (platillo.nombre_platillo))
    
        
#CLASE TEST_MESERO
class test_meseroLista(TestCase):
    
        #POST_MESERO
    def test_post_required_MeseroLista(self):
        pedido = pedido_factory()
        myuser = User.objects.create_user('username', 'example@gmail.com', 'youPassword')
        myuser.save()
        self.client = APIClient()
        self.client.force_authenticate(myuser)
        data = {
            "nombre": "Jorge",
            "apellido_paterno": "Mendez",
            "apellido_materno": "Hernandez",
            "domicilio": "Juan Enriquez 7",
            "email": "jorgemendez.18@gmail.com", 
            "telefono": "7841257896",
            "id_pedido": [1]
        }
        response = self.client.post( '/app-second/mesero',data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEquals(pedido.id, (pedido.id))
        
        #GET_MESERO
    def test_get_required_MeseroDetalle(self):
        pedido = pedido_factory()
        mesero = mesero_factory()
        myuser = User.objects.create_user('username', 'example@gmail.com', 'youPassword')
        myuser.save()
        self.client = APIClient()
        self.client.force_authenticate(myuser)
        response = self.client.get( '/app-second/mesero/1')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEquals(pedido.id, (pedido.id))
        self.assertEquals(mesero.apellido_materno, (mesero.apellido_materno))
        
        #DELETE_MESERO
    def test_delete_required_MeseroDetalle(self):
        myuser = User.objects.create_user('username', 'example@gmail.com', 'youPassword')
        myuser.save()
        self.client = APIClient()
        self.client.force_authenticate(myuser)
        mesero = mesero_factory()
        response = self.client.delete( '/app-second/mesero/1')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEquals(mesero.apellido_paterno, (mesero.apellido_paterno))
        
        #PUT_MESERO
    def test_put_required_MeseroDetalle(self):
        pedido = pedido_factory()
        mesero = mesero_factory()
        myuser = User.objects.create_user('username', 'example@gmail.com', 'youPassword')
        myuser.save()
        self.client = APIClient()
        self.client.force_authenticate(myuser)
        data = {
            "nombre": "Jorge Fernando",
            "apellido_paterno": "Mendez",
            "apellido_materno": "Hernandez",
            "domicilio": "Juan Enriquez 7",
            "email": "jorgemendez.18@gmail.com", 
            "telefono": "7841257896",
            "id_pedido": [1]
        }
        response = self.client.put( '/app-second/mesero/1',data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEquals(pedido.id, (pedido.id))
        self.assertEquals(mesero.nombre, (mesero.nombre))
        

#CLASE TEST_FACTURA
class test_facturaLista(TestCase):
    
        #POST_FACTURA
    def test_post_required_FacturaLista(self):
        pedido = pedido_factory()
        myuser = User.objects.create_user('username', 'example@gmail.com', 'youPassword')
        myuser.save()
        self.client = APIClient()
        self.client.force_authenticate(myuser)
        data = {
            "importe": 400,
            "id_pedido": [1]
        }
        response = self.client.post( '/app-second/factura',data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEquals(pedido.id, (pedido.id))
        
        #GET_FACTURA
    def test_get_required_FacturaDetalle(self):
        pedido = pedido_factory()
        factura = factura_factory()
        myuser = User.objects.create_user('username', 'example@gmail.com', 'youPassword')
        myuser.save()
        self.client = APIClient()
        self.client.force_authenticate(myuser)
        response = self.client.get( '/app-second/factura/1')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEquals(pedido.id, (pedido.id))
        self.assertEquals(factura.id, (factura.id))
        
        #DELETE_FACTURA
    def test_delete_required_FacturaDetalle(self):
        myuser = User.objects.create_user('username', 'example@gmail.com', 'youPassword')
        myuser.save()
        self.client = APIClient()
        self.client.force_authenticate(myuser)
        factura = factura_factory()
        response = self.client.delete( '/app-second/factura/1')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEquals(factura.id, (factura.id))
        
        #PUT_FACTURA
    def test_put_required_FacturaDetalle(self):
        pedido = pedido_factory()
        factura = factura_factory()
        myuser = User.objects.create_user('username', 'example@gmail.com', 'youPassword')
        myuser.save()
        self.client = APIClient()
        self.client.force_authenticate(myuser)
        data = {
            "importe": 600,
            "id_pedido": [1]
        }
        response = self.client.put( '/app-second/factura/1',data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEquals(pedido.id, (pedido.id))
        self.assertEquals(factura.id, (factura.id))
        


#CLASE CONSULTA
class Test_Consultas(TestCase):
    
        #CONSULTA
    def test_filter_required_consulta_mesas_por_num_personas(self):
        mesa = mesa_factory(num_personas=5)
        print(mesa.num_personas)
        myuser = User.objects.create_user('username', 'example@gmail.com', 'youPassword')
        myuser.save()
        self.client = APIClient()
        self.client.force_authenticate(myuser)
        consulta = consulta_mesas_por_num_personas(5)
        print(consulta[0].get("num_personas"))
        print(consulta)
        self.assertEquals(mesa.id_pedido, (mesa.id_pedido))

        
      #CONSULTA
    def test_get_required_consulta_pedidos_por_mesero(self):
        mesero = mesero_factory(id=4)
        print(mesero.id)
        myuser = User.objects.create_user('username', 'example@gmail.com', 'youPassword')
        myuser.save()
        self.client = APIClient()
        self.client.force_authenticate(myuser)
        consulta =consulta_pedidos_por_mesero(4)
        print(consulta)
        self.assertEquals(mesero.nombre, (mesero.nombre))
        
    #CONSULTA
    def test_get_required_consulta_pedidos_por_mesa(self):
        mesa = mesa_factory(id=3)
        print(mesa.id)
        myuser = User.objects.create_user('username', 'example@gmail.com', 'youPassword')
        myuser.save()
        self.client = APIClient()
        self.client.force_authenticate(myuser)
        consulta =consulta_pedidos_por_mesa(3)
        self.assertEquals(mesa.num_personas, (mesa.num_personas))
        print(consulta)
        
     #CONSULTA
    def test_get_required_consulta_pedidos_por_cliente(self):
        pedido = pedido_factory(id=2)
        print(pedido.id)
        myuser = User.objects.create_user('username', 'example@gmail.com', 'youPassword')
        myuser.save()
        self.client = APIClient()
        self.client.force_authenticate(myuser)
        consulta =consulta_pedidos_por_cliente(2)
        self.assertEquals(pedido.id_cliente, (pedido.id_cliente))
        print(consulta)
        
      #CONSULTA
    def test_required_consulta_top_clientes(self):
        pedido = pedido_factory()
        print(pedido.id)
        myuser = User.objects.create_user('username', 'example@gmail.com', 'youPassword')
        myuser.save()
        self.client = APIClient()
        self.client.force_authenticate(myuser)
        consulta = consulta_top_clientes()
        print(consulta)
        self.assertEquals(pedido.cant_pedidos, (pedido.cant_pedidos))
        
     #CONSULTA
    def test_required_consulta_top_platillos(self):
        pedido = pedido_factory()
        print(pedido.id)
        myuser = User.objects.create_user('username', 'example@gmail.com', 'youPassword')
        myuser.save()
        self.client = APIClient()
        self.client.force_authenticate(myuser)
        consulta = consulta_top_platillos()
        print(consulta)
        self.assertEquals(pedido.cant_pedidos, (pedido.cant_pedidos))
        
     #CONSULTA
    def test_required_consulta_mesas_con_mas_de_cin_personas(self):
        mesa = mesa_factory()
        print(mesa.num_personas)
        myuser = User.objects.create_user('username', 'example@gmail.com', 'youPassword')
        myuser.save()
        self.client = APIClient()
        self.client.force_authenticate(myuser)
        consulta = consulta_mesas_con_mas_de_cin_personas()
        print(consulta)
        self.assertEquals(mesa.num_personas, (mesa.num_personas))
        
     
        
     
  
       




        
       


# Create your tests here.
