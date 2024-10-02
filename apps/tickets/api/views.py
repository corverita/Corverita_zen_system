from django.http import Http404

from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from rest_framework.response import Response
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth.models import AnonymousUser

from apps.core.api.views import GenericCatalogBaseViewSet
from apps.core.permissions import *
from apps.usuarios.permissions import *

from rest_framework.exceptions import NotFound
from django.core.exceptions import ObjectDoesNotExist

from ..models import *
from ..permissions import *
from .serializers import *

# ViewSet para el modelo de Ticket
class TicketViewSet(GenericCatalogBaseViewSet):
    queryset = Ticket.objects.all()
    serializer_get = BaseTicketSerializer
    search_fields = ['titulo', 'descripcion']
    ordering_fields = ['titulo', 'descripcion', 'prioridad', 'estatus', 'usuario', 'fecha_creacion', 'fecha_modificacion']
    filterset_fields = ['prioridad', 'estatus', 'usuario']

    def get_serializer_class(self):
        if self.action in ['create', 'update']:
            return PostTicketSerializer
        if self.action in ['list', 'retrieve']:
            return BaseTicketSerializer
        if self.action == 'destroy':
            return DeleteTicketSerializer
        if self.action == 'asignar_prioridad':
            return AsignarPrioridadTicket
        if self.action == 'marcar_solucionado':
            return MarcarSolucionadoTicket
        return self.serializer_get
    
    def get_permissions(self):
        try:
            if self.request.user.is_authenticated:
                perfil = self.request.user.perfil
        except ObjectDoesNotExist:
            raise NotFound(detail="El usuario no tiene un perfil asociado.")

        if self.action in ['list', 'retrieve']:
            return [PuedeVerTickets()]
        if self.action == 'create':
            return [PuedeCrearTickets()]
        if self.action == 'update':
            return [PuedeEditarTickets()]
        if self.action == 'destroy':
            return [PuedeEliminarTickets()]
        if self.action == 'asignar_prioridad':
            return [PuedeAsignarPrioridad()]
        if self.action == 'marcar_solucionado':
            return [PuedeMarcarSolucionado()]
        return super().get_permissions()
    
    def get_queryset(self):
        if not self.request.user.is_authenticated or not hasattr(self.request.user, 'perfil'):
            return Ticket.objects.none()
        if self.request.user.perfil.rol.nombre in ['Admin', 'Soporte']:
            return super().get_queryset()
        return super().get_queryset().filter(usuario=self.request.user)
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, context={'usuario': request.user})
        if serializer.is_valid():
            ticket = serializer.save(usuario=request.user)
            return Response(self.serializer_get(instance = ticket).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @action(detail=True, methods=['put'])
    def asignar_prioridad(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, context={'usuario': request.user})
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        ticket = self.get_object()
        prioridad = Prioridad.objects.get(pk=serializer.validated_data['prioridad'])
        ticket.prioridad = prioridad
        ticket.save()
        return Response(self.serializer_get(instance = ticket).data, status=status.HTTP_200_OK)
    
    @action(detail=True, methods=['post'])
    def marcar_solucionado(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, context={'usuario': request.user})
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        estatus_solucionado = Estatus.objects.get(nombre='Solucionado')
        
        ticket = self.get_object()
        if ticket.estatus == estatus_solucionado:
            return Response({'detail': 'El ticket ya se encuentra solucionado'}, status=status.HTTP_400_BAD_REQUEST)
        
        ticket.estatus = estatus_solucionado
        ticket.save()
        return Response(self.serializer_get(instance = ticket).data, status=status.HTTP_200_OK)
    
class ComentarioViewSet(GenericCatalogBaseViewSet):
    queryset = Comentario.objects.all()
    serializer_get = BaseComentarioSerializer
    search_fields = ['comentario']
    ordering_fields = ['comentario', 'usuario', 'fecha_creacion', 'fecha_modificacion']
    filterset_fields = ['ticket', 'usuario']

    def get_serializer_class(self):
        if self.action in ['create']:
            return PostComentarioSerializer
        if self.action in ['update']:
            return UpdateComentarioSerializer
        if self.action in ['list', 'retrieve']:
            return BaseComentarioSerializer
        if self.action == 'destroy':
            return DeleteComentarioSerializer
        return self.serializer_get
    
    def get_permissions(self):
        try:
            if self.request.user.is_authenticated:
                perfil = self.request.user.perfil
        except ObjectDoesNotExist:
            raise NotFound(detail="El usuario no tiene un perfil asociado.")

        if self.action in ['list', 'retrieve']:
            return [PuedeVerComentarios()]
        if self.action == 'create':
            return [PuedeCrearComentarios()]
        if self.action == 'update':
            return [PuedeEditarComentarios() and EsOwner()]
        if self.action == 'destroy':
            return [PuedeEliminarComentarios() or EsOwner()]
        return super().get_permissions()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, context={'usuario': request.user})
        if serializer.is_valid():
            comentario = serializer.save(usuario=request.user)
            return Response(self.serializer_get(instance = comentario).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)