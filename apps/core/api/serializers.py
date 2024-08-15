from rest_framework import serializers

from ..models import *

# Serializer base para los catálogos del proyecto
class GetCatalogoSerializer(serializers.ModelSerializer):
    class Meta:
        abstract = True
        fields = ['id', 'nombre', 'descripcion']

class CatalogoSerializer(serializers.ModelSerializer):
    class Meta:
        abstract = True
        fields = ['nombre', 'descripcion']

class DeleteCatalogoSerializer(serializers.Serializer):
    class Meta:
        abstract = True
        fields = ['id']