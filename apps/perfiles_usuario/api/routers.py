from rest_framework.routers import DefaultRouter

from .views import PerfilUsuarioViewSet

router = DefaultRouter()

router.register(prefix='perfil_usuario', viewset=PerfilUsuarioViewSet, basename='perfil_usuario')