from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from rest_framework.response import Response
from rest_framework.filters import SearchFilter, OrderingFilter

from datetime import datetime

from apps.core.pagination import Paginador

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
        return self.serializer_class

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
            instance.fecha_modificacion = datetime.now() # Actualización de la fecha de modificación de la instancia
            instance = instance.save()
            return Response(self.serializer_get(instance = instancia).data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)