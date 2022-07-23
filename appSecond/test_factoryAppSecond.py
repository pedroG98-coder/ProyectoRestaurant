import email
from factory.django import DjangoModelFactory
import factory
from appSecond import models

#Cliente Factory
class cliente_factory(DjangoModelFactory):
    class Meta: 
        model = models.Cliente
    nombre = factory.Faker("first_name")
    apellido_paterno = factory.Faker("first_name")
    apellido_materno = factory.Faker("first_name")
    calle = factory.Faker("first_name")
    ciudad = factory.Faker("first_name")
    email = factory.Faker("first_name")
    cp = factory.Faker("first_name")
    telefono = factory.Faker("first_name")
    fecha_elaboracion = factory.Faker("date")
    estatus_sistema = True
    ultima_actualizacion = factory.Faker("date")
    
    
#Pedido Factory    
class pedido_factory(DjangoModelFactory):
        
    class Meta: 
        model = models.Pedido
        
    cant_pedidos = factory.Faker("pyint")
    @factory.post_generation
    def id_cliente(self, create, extracted, **kwargs):
        
        if not create:
            return

        if extracted:
            print(extracted)
            for id in extracted:
                self.id_cliente.add(id)
                
    fecha_elaboracion = factory.Faker("date")
    estatus_sistema = True
    ultima_actualizacion = factory.Faker("date")
    
#Mesa Factory
class mesa_factory(DjangoModelFactory):
    class Meta: 
        model = models.Mesa
    num_personas = factory.Faker("pyint")
    id_cliente = factory.SubFactory(cliente_factory)
    @factory.post_generation
    def id_pedido(self, create, extracted, **kwargs):
        
        if not create:
            return

        if extracted:
            for id in extracted:
                self.id_pedido.add(id)  
    fecha_elaboracion = factory.Faker("date")
    estatus_sistema = True
    ultima_actualizacion = factory.Faker("date")
    
#Pedido Platillo    
class platillo_factory(DjangoModelFactory):
        
    class Meta: 
        model = models.Platillo
    
    nombre_platillo = factory.Faker("first_name")
    precio_platillo = factory.Faker("pyint")
    bebida = factory.Faker("first_name")
    precio_bebida = factory.Faker("pyint")
    @factory.post_generation
    def id_pedido(self, create, extracted, **kwargs):
        
        if not create:
            return

        if extracted:
            for id in extracted:
                self.id_pedido.add(id)  
    descripcion = factory.Faker("first_name")
    fecha_elaboracion = factory.Faker("date")
    estatus_sistema = True
    ultima_actualizacion = factory.Faker("date")
    
#Pedido Mesero    
class mesero_factory(DjangoModelFactory):
        
    class Meta: 
        model = models.Mesero
    
    nombre = factory.Faker("first_name")
    apellido_paterno = factory.Faker("first_name")
    apellido_materno = factory.Faker("first_name")
    domicilio = factory.Faker("first_name")
    email = factory.Faker("first_name")
    telefono = factory.Faker("first_name")
    @factory.post_generation
    def id_pedido(self, create, extracted, **kwargs):
        """
        if not create:
            return"""

        if extracted:
            for id in extracted:
                self.id_pedido.add(id)  
    fecha_elaboracion = factory.Faker("date")
    estatus_sistema = True
    ultima_actualizacion = factory.Faker("date")

#Pedido Factura    
class factura_factory(DjangoModelFactory):
        
    class Meta: 
        model = models.Factura
    
    importe = factory.Faker("pyint")
    @factory.post_generation
    def id_pedido(self, create, extracted, **kwargs):
        
        if not create:
            return

        if extracted:
            for id in extracted:
                self.id_pedido.add(id)  
    fecha_elaboracion = factory.Faker("date")
    estatus_sistema = True
    ultima_actualizacion = factory.Faker("date")
    

               
        
        
    
    

    
    