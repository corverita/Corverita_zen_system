from rest_framework import serializers

from ..models import PerfilUsuario
from apps.usuarios.api.serializers import GetUsuarioSerializer

# Serializer para el perfil de un modelo de Usuario
class PerfilUsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = PerfilUsuario
        fields = ['biografia', 'fecha_nacimiento', 'telefono']

class GetPerfilUsuarioSerializer(serializers.ModelSerializer):
    usuario = GetUsuarioSerializer()

    class Meta:
        model = PerfilUsuario
        fields = ['usuario', 'biografia', 'fecha_nacimiento', 'telefono']