from django.db import models

from apps.catalogos.models import TipoMovimiento
from apps.usuarios.models import Usuario

# Create your models here.

class Producto(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(max_length=500, blank=True)
    stock = models.IntegerField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        ordering = ['id']

class HistorialMovimientoInventario(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    tipo_movimiento = models.ForeignKey(TipoMovimiento, on_delete=models.CASCADE)
    stock = models.IntegerField()
    cantidad = models.IntegerField()
    fecha_movimiento = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['id']