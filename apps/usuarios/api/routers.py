from rest_framework.routers import DefaultRouter

from ..models import Usuario
from .views import RegistroUsuario

router = DefaultRouter()

# # Sprint 10
# router.register(prefix='registrar_usuario', viewset=RegistroUsuario, basename='registrar_usuario')