from rest_framework.generics import GenericAPIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from django.contrib.auth import authenticate

from ..models import Usuario
from .serializers import RegistroUsuarioSerializer, LoginUsuarioSerializer

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
            })
        
        return Response({"message": "Los datos no son correctos"}, status=status.HTTP_400_BAD_REQUEST)