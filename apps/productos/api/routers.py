from rest_framework.routers import DefaultRouter

from .views import *

router = DefaultRouter()

router.register(r'productos', ProductoViewSet, basename='productos')
router.register(r'historial-movimientos-inventario', HistorialMovimientoInventarioViewSet, basename='historial-movimientos-inventario')