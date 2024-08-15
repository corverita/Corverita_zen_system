from rest_framework import serializers

from ..models import *

# Serializer para el catálogo de Estatus
# Serializer Base para Get y respuestas
class BaseEstatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estatus
        fields = ['id', 'nombre', 'descripcion']

# Serializer para recibir información de POST
class PostEstatusSerializer(BaseEstatusSerializer):
    class Meta(BaseEstatusSerializer.Meta):
        fields = ['nombre', 'descripcion']

# Serializer para recibir información de DELETE
class DeleteEstatusSerializer(BaseEstatusSerializer):
    class Meta(BaseEstatusSerializer.Meta):
        fields = ['id']

# Serializers para el catálogo de Prioridad
# Serializer Base para Get y respuestas
class BasePrioridadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prioridad
        fields = ['id', 'nombre', 'descripcion']

# Serializer para recibir información de POST
class PostPrioridadSerializer(BasePrioridadSerializer):
    class Meta(BasePrioridadSerializer.Meta):
        fields = ['nombre', 'descripcion']

# Serializer para recibir información de DELETE
class DeletePrioridadSerializer(BasePrioridadSerializer):
    class Meta(BasePrioridadSerializer.Meta):
        fields = ['id']

# Serializers para el catálogo de TipoMovimiento
# Serializer Base para Get y respuestas
class BaseTipoMovimientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoMovimiento
        fields = ['id', 'nombre', 'descripcion']

# Serializer para recibir información de POST
class PostTipoMovimientoSerializer(BaseTipoMovimientoSerializer):
    class Meta(BaseTipoMovimientoSerializer.Meta):
        fields = ['nombre', 'descripcion']

# Serializer para recibir información de DELETE
class DeleteTipoMovimientoSerializer(BaseTipoMovimientoSerializer):
    class Meta(BaseTipoMovimientoSerializer.Meta):
        fields = ['id']