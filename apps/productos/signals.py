from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Producto, HistorialMovimientoInventario
from apps.catalogos.models import TipoMovimiento


# Esta signal se encarga de detectar los movimientos de inventario de un producto y registrarlos en el historial.
@receiver(post_save, sender=Producto)
def detectar_movimiento_inventario(sender, instance, created, **kwargs):
    # Obtenemos los tipos de movimiento de nuestro catálogo, esperando que la base de datos ya esté lista para no provocar errores.
    try:
        movimiento_entrada = TipoMovimiento.objects.get(nombre='Entrada')
    except TipoMovimiento.DoesNotExist:
        movimiento_entrada = TipoMovimiento.objects.create(nombre='Entrada', descripcion="Entrada de inventario")

    try:
        movimiento_salida = TipoMovimiento.objects.get(nombre='Salida')
    except TipoMovimiento.DoesNotExist:
        movimiento_salida = TipoMovimiento.objects.create(nombre='Salida', descripcion="Salida de inventario")
    
    tipo_movimiento = None
    cantidad = instance.stock
    if created:
        HistorialMovimientoInventario.objects.create(
            producto=instance,
            tipo_movimiento=movimiento_entrada,
            stock=instance.stock,
            cantidad = cantidad
        )
    else:
        historial_anterior = HistorialMovimientoInventario.objects.filter(producto=instance).latest('fecha_movimiento')
        if instance.stock > historial_anterior.stock:
            tipo_movimiento = movimiento_entrada
        elif instance.stock < historial_anterior.stock:
            tipo_movimiento = movimiento_salida

        if tipo_movimiento:
            cantidad = abs(instance.stock - historial_anterior.stock)
            HistorialMovimientoInventario.objects.create(
                producto=instance,
                tipo_movimiento=tipo_movimiento,
                stock=abs(instance.stock),
                cantidad = cantidad
            )
