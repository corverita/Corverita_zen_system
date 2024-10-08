from rest_framework import serializers

from apps.catalogos.api.serializers import BaseTipoMovimientoSerializer
from ..models import *

# Serializer para el catálogo de Producto
# Serializer Base para Get y respuestas
class BaseProductoSerializer(serializers.ModelSerializer):
    fecha_creacion = serializers.DateTimeField(format='%d-%m-%Y %H:%M:%S', read_only=True)
    fecha_modificacion = serializers.DateTimeField(format='%d-%m-%Y %H:%M:%S', read_only=True)
    precio = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)

    class Meta:
        model = Producto
        fields = ['id', 'nombre', 'descripcion', 'stock', 'fecha_creacion', 'fecha_modificacion', 'precio']

# Serializer para recibir información de POST
class PostProductoSerializer(BaseProductoSerializer):
    precio = serializers.DecimalField(max_digits=10, decimal_places=2)
    class Meta(BaseProductoSerializer.Meta):
        fields = ['nombre', 'descripcion', 'stock', 'precio']

# Serializer para recibir información de DELETE
class DeleteProductoSerializer(BaseProductoSerializer):
    class Meta(BaseProductoSerializer.Meta):
        fields = ['id']

class RestockProductoSerializer(serializers.ModelSerializer):
    cantidad = serializers.IntegerField()

    class Meta:
        model = Producto
        fields = ['id', 'cantidad']

    def update(self, instance, validated_data):
        instance.stock += validated_data.get('cantidad')
        instance.save()
        return instance
    
class VendidoProductoSerializer(serializers.ModelSerializer):
    cantidad = serializers.IntegerField()

    class Meta:
        model = Producto
        fields = ['id', 'cantidad']

    def validate_cantidad(self, value):
        if value > self.instance.stock:
            raise serializers.ValidationError('No hay suficiente stock para realizar la venta')
        return value

    def update(self, instance, validated_data):
        instance.stock -= validated_data.get('cantidad')
        instance.save()
        return instance

# Serializer para el historial de movimientos de inventario
class HistorialMovimientoInventarioSerializer(serializers.ModelSerializer):
    fecha_movimiento = serializers.DateTimeField(format='%d-%m-%Y %H:%M:%S', read_only=True)
    producto = BaseProductoSerializer(read_only=True)
    tipo_movimiento = BaseTipoMovimientoSerializer(read_only=True)

    class Meta:
        model = HistorialMovimientoInventario
        fields = ['id', 'producto', 'tipo_movimiento', 'cantidad', 'fecha_movimiento']