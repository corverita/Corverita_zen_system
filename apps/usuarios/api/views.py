from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import GenericAPIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import action

from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenBlacklistView
from rest_framework_simplejwt.exceptions import TokenError

from django.contrib.auth import authenticate

from ..models import Usuario, PerfilUsuario
from .serializers import *

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
        
        return Response({"message": "Los datos no son correctos"}, status=status.HTTP_400_BAD_REQUEST)
    
class LogoutView(TokenBlacklistView):
    
    def post(self, request):
        if not request.data.get('refresh'):
            return Response({"message": "No se ha iniciado sesión"}, status=status.HTTP_400_BAD_REQUEST)
        
        refresh_token = request.data.get('refresh')
        try:
            token = RefreshToken(refresh_token)
        except TokenError as e:
            return Response({"message": "Token no válido o este ya ha sido eliminado anteriormente"}, status=status.HTTP_400_BAD_REQUEST)
        
        token.blacklist()
        return Response({"message": "Token eliminado"}, status=status.HTTP_200_OK)
        
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
        return self.request.user.perfil
    
    # Método POST
    def create(self, request, *args, **kwargs):
        if self.get_object():
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