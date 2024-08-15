from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import GenericAPIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import action

from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenBlacklistView
from rest_framework_simplejwt.exceptions import TokenError

from django.contrib.auth import authenticate

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