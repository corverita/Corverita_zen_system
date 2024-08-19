from django.apps import AppConfig

class ProductosConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.productos'
    
    def ready(self):
        from .signals import detectar_movimiento_inventario