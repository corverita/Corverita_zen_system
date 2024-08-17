from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import NotFound
from django.core.exceptions import ObjectDoesNotExist

from ..models import PerfilUsuario
from .serializers import *

from apps.usuarios.permissions import *
from apps.core.permissions import EsOwner
from apps.usuarios.models import Rol

class PerfilUsuarioViewSet(ModelViewSet):
    queryset = PerfilUsuario.objects.all()
    serializer_class = PerfilUsuarioSerializer
    http_method_names = ['get', 'post', 'put']

    def get_serializer_class(self):
        if self.action in ['create', 'update']:
            return PerfilUsuarioSerializer
        if self.action in ['list', 'retrieve']:
            return GetPerfilUsuarioSerializer
        if self.action == 'asignar_rol':
            return AsignarRolSerializer
        return self.serializer_class
    
    def get_permissions(self):
        try:
            if self.request.user.is_authenticated:
                perfil = self.request.user.perfil
        except ObjectDoesNotExist:
            raise NotFound(detail="El usuario no tiene un perfil asociado.")
        
        if self.action in ['list', 'retrieve']:
            return [IsAuthenticated()]
        if self.action in ['create']:
            return [IsAuthenticated()]
        if self.action in ['update_profile']:
            return [EsOwner()]
        if self.action == 'asignar_rol':
            return [EsSuperUsuario() or (EsAdmin() or EsSoporte())]
        return super().get_permissions

    def get_queryset(self):
        if not self.request.user.is_authenticated or not hasattr(self.request.user, 'perfil'):
            return PerfilUsuario.objects.none()
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
            return Response({"detail": "El usuario ya tiene un perfil"}, status=status.HTTP_400_BAD_REQUEST)
        
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
    
    @action(detail=False, methods=['post'])
    def asignar_rol(self, request, *args, **kwargs):
        serializer = AsignarRolSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        perfil = serializer.save()
        return Response(GetPerfilUsuarioSerializer(instance = perfil).data, status=status.HTTP_200_OK)