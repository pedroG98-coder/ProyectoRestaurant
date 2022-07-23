from django.shortcuts import render
from appSecond import models, serializers
from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

#Vista Clase clienteLista

class clienteLista(APIView):
    """
    -Get retorna todos los registros en la bd con estatus en sistema = True
    -Post permite crear un nuevo registro en la base de datos
    """
    permission_classes = [IsAuthenticated]
    def get(self, request):
        objetos = models.Cliente.objects.filter(estatus_sistema=True)
        serializer = serializers.clienteSerializer(objetos, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = serializers.clienteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  
    
#Vista Clase clienteDetalle

class clienteDetalle(APIView):
    """
    -Esta ruta espera recibir un entero pk (llave primaria)
    -Get object busca una instancia basado en la pk
    -Get utiliza get object para retornar una sola instancia serializada
    -Put permite actualizar el objeto seleccionado con la pk
    -Delete cambia el estatus de estatus en sistema (Por definición no existe un método para borrar registros)
    """
    permission_classes = [IsAuthenticated]
    def get_object(self, pk):
        objeto = get_object_or_404(models.Cliente, pk=pk)
        return objeto

    def get(self, request, pk):
        objeto = self.get_object(pk)
        serializer = serializers.clienteSerializer(objeto)
        return Response(serializer.data)

    def put(self, request, pk):
        objeto = self.get_object(pk)
        serializer = serializers.clienteSerializer(objeto, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        objeto = self.get_object(pk)
        objeto.estatus_sistema = False
        objeto.save()
        return Response(status=status.HTTP_204_NO_CONTENT) 
    
#Vista Clase mesaLista

class mesaLista(APIView):
    """
    -Get retorna todos los registros en la bd con estatus en sistema = True
    -Post permite crear un nuevo registro en la base de datos
    """
    permission_classes = [IsAuthenticated]
    def get(self, request):
        objetos = models.Mesa.objects.filter(estatus_sistema=True)
        serializer = serializers.mesaSerializer(objetos, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = serializers.mesaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  
    
    
#Vista Clase mesaDetalle

class mesaDetalle(APIView):
    """
    -Esta ruta espera recibir un entero pk (llave primaria)
    -Get object busca una instancia basado en la pk
    -Get utiliza get object para retornar una sola instancia serializada
    -Put permite actualizar el objeto seleccionado con la pk
    -Delete cambia el estatus de estatus en sistema (Por definición no existe un método para borrar registros)
    """
    permission_classes = [IsAuthenticated]
    def get_object(self, pk):
        objeto = get_object_or_404(models.Mesa, pk=pk)
        return objeto

    def get(self, request, pk):
        objeto = self.get_object(pk)
        serializer = serializers.mesaSerializer(objeto)
        return Response(serializer.data)

    def put(self, request, pk):
        objeto = self.get_object(pk)
        serializer = serializers.mesaSerializer(objeto, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        objeto = self.get_object(pk)
        objeto.estatus_sistema = False
        objeto.save()
        return Response(status=status.HTTP_204_NO_CONTENT) 

#Vista Clase pedidoLista

class pedidoLista(APIView):
    """
    -Get retorna todos los registros en la bd con estatus en sistema = True
    -Post permite crear un nuevo registro en la base de datos
    """
    permission_classes = [IsAuthenticated]
    def get(self, request):
        objetos = models.Pedido.objects.filter(estatus_sistema=True)
        serializer = serializers.pedidoSerializer(objetos, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = serializers.pedidoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  

#Vista Clase pedidoDetalle

class pedidoDetalle(APIView):
    """
    -Esta ruta espera recibir un entero pk (llave primaria)
    -Get object busca una instancia basado en la pk
    -Get utiliza get object para retornar una sola instancia serializada
    -Put permite actualizar el objeto seleccionado con la pk
    -Delete cambia el estatus de estatus en sistema (Por definición no existe un método para borrar registros)
    """
    permission_classes = [IsAuthenticated]
    def get_object(self, pk):
        objeto = get_object_or_404(models.Pedido, pk=pk)
        return objeto

    def get(self, request, pk):
        objeto = self.get_object(pk)
        serializer = serializers.pedidoSerializer(objeto)
        return Response(serializer.data)

    def put(self, request, pk):
        objeto = self.get_object(pk)
        serializer = serializers.pedidoSerializer(objeto, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        objeto = self.get_object(pk)
        objeto.estatus_sistema = False
        objeto.save()
        return Response(status=status.HTTP_204_NO_CONTENT) 
    
#Vista Clase platilloLista

class platilloLista(APIView):
    """
    -Get retorna todos los registros en la bd con estatus en sistema = True
    -Post permite crear un nuevo registro en la base de datos
    """
    permission_classes = [IsAuthenticated]
    def get(self, request):
        objetos = models.Platillo.objects.filter(estatus_sistema=True)
        serializer = serializers.platilloSerializer(objetos, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = serializers.platilloSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
    
#Vista Clase platilloDetalle

class platilloDetalle(APIView):
    """
    -Esta ruta espera recibir un entero pk (llave primaria)
    -Get object busca una instancia basado en la pk
    -Get utiliza get object para retornar una sola instancia serializada
    -Put permite actualizar el objeto seleccionado con la pk
    -Delete cambia el estatus de estatus en sistema (Por definición no existe un método para borrar registros)
    """
    permission_classes = [IsAuthenticated]
    def get_object(self, pk):
        objeto = get_object_or_404(models.Platillo, pk=pk)
        return objeto

    def get(self, request, pk):
        objeto = self.get_object(pk)
        serializer = serializers.platilloSerializer(objeto)
        return Response(serializer.data)

    def put(self, request, pk):
        objeto = self.get_object(pk)
        serializer = serializers.platilloSerializer(objeto, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        objeto = self.get_object(pk)
        objeto.estatus_sistema = False
        objeto.save()
        return Response(status=status.HTTP_204_NO_CONTENT) 
    
#Vista Clase meseroLista

class meseroLista(APIView):
    """
    -Get retorna todos los registros en la bd con estatus en sistema = True
    -Post permite crear un nuevo registro en la base de datos
    """
    permission_classes = [IsAuthenticated]
    def get(self, request):
        objetos = models.Mesero.objects.filter(estatus_sistema=True)
        serializer = serializers.meseroSerializer(objetos, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = serializers.meseroSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
    
#Vista Clase meseroDetalle

class meseroDetalle(APIView):
    """
    -Esta ruta espera recibir un entero pk (llave primaria)
    -Get object busca una instancia basado en la pk
    -Get utiliza get object para retornar una sola instancia serializada
    -Put permite actualizar el objeto seleccionado con la pk
    -Delete cambia el estatus de estatus en sistema (Por definición no existe un método para borrar registros)
    """
    permission_classes = [IsAuthenticated]
    def get_object(self, pk):
        objeto = get_object_or_404(models.Mesero, pk=pk)
        return objeto

    def get(self, request, pk):
        objeto = self.get_object(pk)
        serializer = serializers.meseroSerializer(objeto)
        return Response(serializer.data)

    def put(self, request, pk):
        objeto = self.get_object(pk)
        serializer = serializers.meseroSerializer(objeto, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        objeto = self.get_object(pk)
        objeto.estatus_sistema = False
        objeto.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
#Vista Clase facturaLista

class facturaLista(APIView):
    """
    -Get retorna todos los registros en la bd con estatus en sistema = True
    -Post permite crear un nuevo registro en la base de datos
    """
    permission_classes = [IsAuthenticated]
    def get(self, request):
        objetos = models.Factura.objects.filter(estatus_sistema=True)
        serializer = serializers.facturaSerializer(objetos, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = serializers.facturaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
    
#Vista Clase meseroDetalle

class facturaDetalle(APIView):
    """
    -Esta ruta espera recibir un entero pk (llave primaria)
    -Get object busca una instancia basado en la pk
    -Get utiliza get object para retornar una sola instancia serializada
    -Put permite actualizar el objeto seleccionado con la pk
    -Delete cambia el estatus de estatus en sistema (Por definición no existe un método para borrar registros)
    """
    permission_classes = [IsAuthenticated]
    def get_object(self, pk):
        objeto = get_object_or_404(models.Factura, pk=pk)
        return objeto

    def get(self, request, pk):
        objeto = self.get_object(pk)
        serializer = serializers.facturaSerializer(objeto)
        return Response(serializer.data)

    def put(self, request, pk):
        objeto = self.get_object(pk)
        serializer = serializers.facturaSerializer(objeto, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        objeto = self.get_object(pk)
        objeto.estatus_sistema = False
        objeto.save()
        return Response(status=status.HTTP_204_NO_CONTENT) 



# Create your views here.
