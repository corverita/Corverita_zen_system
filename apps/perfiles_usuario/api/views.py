from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import action

from ..models import PerfilUsuario
from .serializers import *

class PerfilUsuarioViewSet(ModelViewSet):
    queryset = PerfilUsuario.objects.all()
    serializer_class = PerfilUsuarioSerializer
    http_method_names = ['get', 'post', 'put']

    def get_serializer_class(self):
        if self.action in ['create', 'update']:
            return PerfilUsuarioSerializer
        if self.action in ['list', 'retrieve']:
            return GetPerfilUsuarioSerializer
        return self.serializer_class

    def get_queryset(self):
        if self.request.user.is_superuser:
            return self.queryset.all()
        return self.queryset.filter(usuario=self.request.user)
    
    def get_object(self):
        if PerfilUsuario.objects.filter(usuario=self.request.user).exists():
            return PerfilUsuario.objects.get(usuario=self.request.user)
        return None
    
    # Método POST
    def create(self, request, *args, **kwargs):
        if self.get_object() != None:
            return Response({"message": "El usuario ya tiene un perfil"}, status=status.HTTP_400_BAD_REQUEST)
        
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        perfil = serializer.save(usuario=request.user)
        return Response(GetPerfilUsuarioSerializer(instance = perfil).data, status=status.HTTP_201_CREATED)
    
    # Método UPDATE
    @action(detail=False, methods=['put'], url_path='update-profile')
    def update_profile(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        perfil = serializer.save(usuario=request.user)
        return Response(GetPerfilUsuarioSerializer(instance = perfil).data, status=status.HTTP_200_OK)