from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from rest_framework.response import Response
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.decorators import action
from rest_framework.exceptions import NotFound
from django.core.exceptions import ObjectDoesNotExist

from apps.core.pagination import Paginador
from apps.core.permissions import *
from apps.usuarios.permissions import *

from ..permissions import *
from ..models import *
from .serializers import *

# ViewSet para el modelo de Producto
class ProductoViewSet(ModelViewSet):
    queryset = Producto.objects.all()
    serializer_get = BaseProductoSerializer
    http_method_names = ['get', 'post', 'put', 'delete']
    search_fields = ['nombre', 'descripcion']
    filter_backends = [SearchFilter, OrderingFilter]
    pagination_class = Paginador

    def get_serializer_class(self):
        if self.action in ['create', 'update']:
            return PostProductoSerializer
        if self.action in ['list', 'retrieve']:
            return BaseProductoSerializer
        if self.action == 'destroy':
            return DeleteProductoSerializer
        if self.action == 'restock':
            return RestockProductoSerializer
        if self.action == 'vendido':
            return VendidoProductoSerializer
        return self.serializer_get
    
    def get_permissions(self):
        try:
            if self.request.user.is_authenticated:
                perfil = self.request.user.perfil
        except ObjectDoesNotExist:
            raise NotFound(detail="El usuario no tiene un perfil asociado.")
        
        if self.action in ['list', 'retrieve']:
            return [PuedeVerProducto()]
        if self.action in ['create']:
            return [PuedeCrearProducto()]
        if self.action in ['update']:
            return [PuedeEditarProducto()]
        if self.action in ['destroy']:
            return [PuedeEliminarProducto()]
        if self.action in ['restock']:
            return [PuedeEditarProducto()]
        if self.action in ['vendido']:
            return [PuedeEditarProducto()]
        return super().get_permissions()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            instancia = serializer.save()
            return Response(self.serializer_get(instance = instancia).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        if serializer.is_valid():
            instancia = serializer.save()
            return Response(self.serializer_get(instance = instancia).data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    @action(detail=True, methods=['post'], url_path='restock')
    def restock(self, request, pk=None):
        instance = self.get_object()
        serializer = self.get_serializer(instance=instance, data=request.data)
        if serializer.is_valid():
            instancia = serializer.save()
            return Response(self.serializer_get(instance = instancia).data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @action(detail=True, methods=['post'], url_path='vendido')
    def vendido(self, request, pk=None):
        instance = self.get_object()
        serializer = self.get_serializer(instance=instance, data=request.data)
        if serializer.is_valid():
            instancia = serializer.save()
            return Response(self.serializer_get(instance = instancia).data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class HistorialMovimientoInventarioViewSet(ModelViewSet):
    queryset = HistorialMovimientoInventario.objects.all()
    serializer_class = HistorialMovimientoInventarioSerializer
    http_method_names = ['get']
    pagination_class = Paginador

    def get_permissions(self):
        try:
            if self.request.user.is_authenticated:
                perfil = self.request.user.perfil
        except ObjectDoesNotExist:
            raise NotFound(detail="El usuario no tiene un perfil asociado.")
        
        if self.action in ['list', 'retrieve']:
            return [EsAdmin()]
