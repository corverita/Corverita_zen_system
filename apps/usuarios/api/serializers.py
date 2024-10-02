from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from rest_framework.validators import UniqueValidator
from ..models import *

# Serializadores para el modelo Permiso
class PermisoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permiso
        fields = '__all__'

class PostPermisoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permiso
        fields = ['nombre']

class DeletePermisoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permiso
        fields = ['id']

# Serializadores para el modelo Rol
class RolSerializer(serializers.ModelSerializer):
    permisos = PermisoSerializer(many=True)
    class Meta:
        model = Rol
        fields = '__all__'

class PostRolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rol
        fields = ['nombre']

class DeleteRolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rol
        fields = ['id']

class AsignarPermisosRolSerializer(serializers.ModelSerializer):
    permisos = serializers.ListField(child=serializers.IntegerField())
    class Meta:
        model = Rol
        fields = ['permisos']

    def validate_permisos(self, value):
        for permiso in value:
            if not Permiso.objects.filter(pk=permiso).exists():
                raise serializers.ValidationError(f"El permiso '{permiso}' no existe")
        return value


# Serializador para el GET del modelo de Usuario
class GetUsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'username', 'first_name', 'last_name', 'email']


# Serializador para el registro de un modelo de Usuario
class RegistroUsuarioSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True, validators=[UniqueValidator(queryset=Usuario.objects.all())])
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password_confirmation = serializers.CharField(write_only=True, required=True)
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)

    class Meta:
        model = Usuario
        fields = ['username', 'first_name', 'last_name', 'email', 'password', 'password_confirmation']

    def validate(self, attrs):
        if attrs['password'] != attrs['password_confirmation']:
            raise serializers.ValidationError({"password": "Las contraseñas no coinciden."})
        return attrs

    def create(self, validated_data):
        user = Usuario.objects.create(
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
    
# Serializer para el login de un modelo de Usuario
class LoginUsuarioSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)