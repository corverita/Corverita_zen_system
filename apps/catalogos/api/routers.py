from rest_framework.routers import DefaultRouter

from .views import *

router = DefaultRouter()

router.register(prefix='estatus', viewset=EstatusViewSet, basename='estatus')
router.register(prefix='prioridad', viewset=PrioridadViewSet, basename='prioridad')
router.register(prefix='tipo-movimiento', viewset=TipoMovimientoViewSet, basename='tipo-movimiento')