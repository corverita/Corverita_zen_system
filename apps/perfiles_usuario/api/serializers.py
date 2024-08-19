from rest_framework import serializers

from ..models import PerfilUsuario
from apps.usuarios.models import Rol
from apps.usuarios.api.serializers import GetUsuarioSerializer, RolSerializer

# Serializer para el perfil de un modelo de Usuario
class PerfilUsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = PerfilUsuario
        fields = ['biografia', 'fecha_nacimiento', 'telefono']

class GetPerfilUsuarioSerializer(serializers.ModelSerializer):
    usuario = GetUsuarioSerializer()
    rol = RolSerializer()

    class Meta:
        model = PerfilUsuario
        fields = ['usuario', 'biografia', 'fecha_nacimiento', 'telefono', 'rol']

class AsignarRolSerializer(serializers.Serializer):
    rol = serializers.IntegerField()
    usuario = serializers.IntegerField()
    
    def validate_usuario(self, value):
        if not PerfilUsuario.objects.filter(usuario__id=value).exists():
            raise serializers.ValidationError("El usuario seleccionado no tiene un perfil")
        return value

    def validate_rol(self, value):
        if not Rol.objects.filter(pk=value).exists():
            raise serializers.ValidationError("El rol seleccionado no existe")
        return value
    
    def save(self):
        perfil = PerfilUsuario.objects.get(usuario__id=self.validated_data['usuario'])
        rol = Rol.objects.get(pk=self.validated_data['rol'])
        perfil.rol = rol
        perfil.save()
        return perfil