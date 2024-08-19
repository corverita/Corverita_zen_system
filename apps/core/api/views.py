from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from rest_framework.response import Response
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.exceptions import NotFound
from django_filters.rest_framework import DjangoFilterBackend
from django.core.exceptions import ObjectDoesNotExist

from django.http import Http404

from apps.core.pagination import Paginador
from apps.core.permissions import *
from apps.usuarios.permissions import *
from apps.usuarios.models import Usuario

from ..models import *
from .serializers import *

# ViewSet para el modelo abstracto genérico de catálogos
class GenericCatalogBaseViewSet(ModelViewSet):
    queryset = None
    serializer_get = None
    http_method_names = ['get', 'post', 'put', 'delete']
    search_fields = ['nombre', 'descripcion']
    filter_backends = [SearchFilter, OrderingFilter, DjangoFilterBackend]
    pagination_class = Paginador

    def get_serializer_class(self):
        if self.action in ['create', 'update']:
            return GetCatalogoSerializer
        if self.action in ['list', 'retrieve']:
            return CatalogoSerializer
        if self.action == 'destroy':
            return DeleteCatalogoSerializer
        return self.serializer_get
    
    def get_permissions(self):
        try:
            if self.request.user.is_authenticated:
                perfil = self.request.user.perfil
        except ObjectDoesNotExist:
            raise NotFound(detail="El usuario no tiene un perfil asociado.")
        
        if self.action in ['create', 'update', 'destroy']:
            return [EsAdmin()]
        if self.action in ['list', 'retrieve']:
            return [EsAdmin() or EsSoporte()]
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
        
    def get_object(self):
        try:
            return super().get_object()
        except Http404:
            raise NotFound(detail="El objeto con el id que buscas no existe.")