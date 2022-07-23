from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
#Clase Cliente
    
class Cliente(models.Model):
    """
    guarda los datos de los clientes
    """
    nombre = models.CharField("Nombre(s)", max_length=100)
    apellido_paterno = models.CharField("Apellido Paterno", max_length=100)
    apellido_materno = models.CharField("Apellido Materno", max_length=100)
    calle = models.CharField("Calle", default= "", max_length=50)
    ciudad = models.CharField("Ciudad", default= "", max_length=50)
    email = models.EmailField("Correo electrónico", max_length=254,unique=True)
    cp = models.CharField("Código Postal", default= "", max_length=10)
    telefono = models.CharField("Telefono", default="", max_length=12,unique=True)
    fecha_elaboracion = models.DateTimeField(auto_now_add=True, editable=False)
    estatus_sistema = models.BooleanField(default=True)
    ultima_actualizacion = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return self.nombre
    
    def __unicode__(self):
            return '{} {}'.format(self.email, self.telefono)


    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
        


# Create your models here.

#Clase Pedido
    
class Pedido(models.Model):
    """
    guarda los datos de los pedidos
    """
    cant_pedidos = models.PositiveIntegerField("Cantidad de Pedidos", validators=[MinValueValidator(1), MaxValueValidator(20)])
    id_cliente =models.ManyToManyField(Cliente)
    fecha_elaboracion = models.DateTimeField(auto_now_add=True, editable=False)
    estatus_sistema = models.BooleanField(default=True)
    ultima_actualizacion = models.DateTimeField(auto_now=True, editable=False)

    def __int__(self):
        return self.cant_pedidos

    class Meta:
        verbose_name = "Pedido"
        verbose_name_plural = "Pedidos"
        
#Clase Mesa
    
class Mesa(models.Model):
    """
    guarda los datos de la Mesa
    """
    num_personas = models.PositiveIntegerField("Numero de Personas", validators=[MinValueValidator(1), MaxValueValidator(12)])
    id_cliente =models.ForeignKey(Cliente, on_delete=models.CASCADE)
    id_pedido = models.ManyToManyField(Pedido)
    fecha_elaboracion = models.DateTimeField(auto_now_add=True, editable=False)
    estatus_sistema = models.BooleanField(default=True)
    ultima_actualizacion = models.DateTimeField(auto_now=True, editable=False)

    def __int__(self):
        return self.num_personas

    class Meta:
        verbose_name = "Mesa"
        verbose_name_plural = "Mesas"
        
#Clase Platillos
    
class Platillo(models.Model):
    """
    guarda los datos de los pedidos
    """
    nombre_platillo = models.CharField("Nombre del Platillo", max_length=100, unique=True)
    precio_platillo = models.PositiveIntegerField("Precio del Platillo",validators=[MinValueValidator(1), MaxValueValidator(1000)])
    bebida = models.CharField("Nombre de la Bebida", max_length=100)
    precio_bebida = models.PositiveIntegerField("Precio de la Bebida",validators=[MinValueValidator(1), MaxValueValidator(1000)])
    id_pedido = models.ManyToManyField(Pedido)
    descripcion = models.CharField("Descripción del Platillo", max_length=100)
    fecha_elaboracion = models.DateTimeField(auto_now_add=True, editable=False)
    estatus_sistema = models.BooleanField(default=True)
    ultima_actualizacion = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return self.nombre_platillo
    
    def __unicode__(self):
            return self.nombre_platillo

    class Meta:
        verbose_name = "Platillo"
        verbose_name_plural = "Platillos"
        
#Clase Mesero
    
class Mesero(models.Model):
    """
    guarda los datos de los meseros
    """
    nombre = models.CharField("Nombre(s)", max_length=100)
    apellido_paterno = models.CharField("Apellido Paterno", max_length=100)
    apellido_materno = models.CharField("Apellido Materno", max_length=100)
    domicilio = models.CharField("Domicilio", default= "", max_length=50)
    email = models.EmailField("Correo electrónico", max_length=254)
    telefono = models.CharField("Telefono", default="", max_length=12)
    id_pedido = models.ManyToManyField(Pedido)
    fecha_elaboracion = models.DateTimeField(auto_now_add=True, editable=False)
    estatus_sistema = models.BooleanField(default=True)
    ultima_actualizacion = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return self.nombre
    

    class Meta:
        verbose_name = "Mesero"
        verbose_name_plural = "Meseros"
        
#Clase Factura
    
class Factura(models.Model):
    """
    guarda los datos de las Facturas
    """
    importe = models.PositiveIntegerField("Importe Total", validators=[MinValueValidator(1), MaxValueValidator(100000)])
    id_pedido = models.ManyToManyField(Pedido)
    fecha_elaboracion = models.DateTimeField(auto_now_add=True, editable=False)
    estatus_sistema = models.BooleanField(default=True)
    ultima_actualizacion = models.DateTimeField(auto_now=True, editable=False)

    def __int__(self):
        return self.importe

    class Meta:
        verbose_name = "Factura"
        verbose_name_plural = "Facturas"