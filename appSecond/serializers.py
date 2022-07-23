from rest_framework import serializers
from appSecond import models

class clienteSerializer(serializers.ModelSerializer):
    class Meta:
        ordering = ['id']
        model = models.Cliente
        fields = "__all__"
        depth = 0
        
class mesaSerializer(serializers.ModelSerializer):
    class Meta:
        ordering = ['id']
        model = models.Mesa
        fields = "__all__"
        depth = 0
        
class pedidoSerializer(serializers.ModelSerializer):
    class Meta:
        ordering = ['id']
        model = models.Pedido
        fields = "__all__"
        depth = 0

class platilloSerializer(serializers.ModelSerializer):
    class Meta:
        ordering = ['id']
        model = models.Platillo
        fields = "__all__"
        depth = 0
        
class meseroSerializer(serializers.ModelSerializer):
    class Meta:
        ordering = ['id']
        model = models.Mesero
        fields = "__all__"
        depth = 0
        
class facturaSerializer(serializers.ModelSerializer):
    class Meta:
        ordering = ['id']
        model = models.Factura
        fields = "__all__"
        depth = 0
        

