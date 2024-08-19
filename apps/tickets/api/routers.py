from rest_framework.routers import DefaultRouter

from .views import *

router = DefaultRouter()

router.register(r'tickets', TicketViewSet, basename='tickets')
router.register(r'comentarios', ComentarioViewSet, basename='comentarios')