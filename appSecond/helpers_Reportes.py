
from itertools import count
from django.db.models import Count
from appSecond import models
from appSecond import models, serializers


    #Consult
def consulta_mesas_por_num_personas(num_personas):
    mesas_seleccionadas = models.Mesa.objects.filter(num_personas=num_personas)
    serializer = serializers.mesaSerializer(mesas_seleccionadas, many=True)
    return serializer.data

    #PEDIDO POR MESERO

def consulta_pedidos_por_mesero(id):
    pedidos_mesero = models.Mesero.objects.get(id=id)
    serializer = serializers.meseroSerializer(pedidos_mesero,)
    return serializer.data

  #PEDIDOS POR MESA
def consulta_pedidos_por_mesa(id):
    pedidos_mesa = models.Mesa.objects.get(id=id)
    serializer = serializers.mesaSerializer(pedidos_mesa,)
    return serializer.data

    #PEDIDOS POR ClIENTE
def consulta_pedidos_por_cliente(id):
    pedidos_cliente = models.Pedido.objects.get(id=id)
    serializer = serializers.pedidoSerializer(pedidos_cliente,)
    return serializer.data

    #TOP CLIENTES
def consulta_top_clientes():
    top_cliente = models.Pedido.objects.annotate(top_clientes=Count('cant_pedidos')).order_by('-cant_pedidos')[:3]
    serializer = serializers.pedidoSerializer(top_cliente, many=True)
    return serializer.data


    #TOP PLATILLOS
def consulta_top_platillos():
    top_platillo = models.Pedido.objects.annotate(top_platillos=Count('cant_pedidos')).order_by('-cant_pedidos')[:3]
    serializer = serializers.pedidoSerializer(top_platillo, many=True)
    return serializer.data


#Mesas con mas de 5 personas
def consulta_mesas_con_mas_de_cin_personas():
    num_cinco_personas = models.Mesa.objects.filter(num_personas__gte=5)
    serializer = serializers.mesaSerializer(num_cinco_personas, many=True)
    return serializer.data


    #    from appSecond import helpers_Reportes as hr