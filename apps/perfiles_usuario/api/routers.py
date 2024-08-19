from rest_framework.routers import DefaultRouter

from .views import PerfilUsuarioViewSet

router = DefaultRouter()

router.register(prefix='perfil-usuario', viewset=PerfilUsuarioViewSet, basename='perfil-usuario')