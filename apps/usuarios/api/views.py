from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import GenericAPIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import action

from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenBlacklistView
from rest_framework_simplejwt.exceptions import TokenError

from django.contrib.auth import authenticate

from apps.core.api.views import GenericCatalogBaseViewSet

from .serializers import *
from ..permissions import *

class RegistroUsuario(GenericAPIView):
    serializer_class = RegistroUsuarioSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class LoginView(GenericAPIView):
    serializer_class = LoginUsuarioSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        user = authenticate(email=serializer.validated_data['email'], password=serializer.validated_data['password'])

        if user is not None:
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'user': GetUsuarioSerializer(user).data
            })
        
        return Response({"detail": "Los datos no son correctos"}, status=status.HTTP_400_BAD_REQUEST)
    
class LogoutView(TokenBlacklistView):
    
    def post(self, request):
        if not request.data.get('refresh'):
            return Response({"detail": "No se ha iniciado sesión"}, status=status.HTTP_400_BAD_REQUEST)
        
        refresh_token = request.data.get('refresh')
        try:
            token = RefreshToken(refresh_token)
        except TokenError as e:
            return Response({"detail": "Token no válido o este ya ha sido eliminado anteriormente"}, status=status.HTTP_400_BAD_REQUEST)
        
        token.blacklist()
        return Response({"detail": "Token eliminado"}, status=status.HTTP_200_OK)
    
class PermisoViewSet(GenericCatalogBaseViewSet):
    queryset = Permiso.objects.all()
    serializer_get = PermisoSerializer
    search_fields = ['nombre']
    filterset_fields = []

    def get_serializer_class(self):
        if self.action in ['create', 'update']:
            return PostPermisoSerializer
        if self.action in ['list', 'retrieve']:
            return PermisoSerializer
        if self.action == 'destroy':
            return DeletePermisoSerializer
        return self.serializer_get

class RolViewSet(GenericCatalogBaseViewSet):
    queryset = Rol.objects.all()
    serializer_get = RolSerializer
    search_fields = ['nombre', 'permisos__nombre']
    filterset_fields = ['permisos']

    def get_serializer_class(self):
        if self.action in ['create', 'update']:
            return PostRolSerializer
        if self.action in ['list', 'retrieve']:
            return RolSerializer
        if self.action == 'destroy':
            return DeleteRolSerializer
        if self.action == 'asignar_permisos':
            return AsignarPermisosRolSerializer
        return self.serializer_get
    
    @action(detail=True, methods=['put'])
    def asignar_permisos(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        rol = self.get_object()
        permisos = Permiso.objects.filter(pk__in=serializer.validated_data['permisos'])
        rol.permisos.set(permisos)
        return Response(self.serializer_get(instance = rol).data, status=status.HTTP_200_OK)