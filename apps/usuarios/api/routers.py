from rest_framework.routers import DefaultRouter

from .views import *

router = DefaultRouter()

router.register(r'permisos', PermisoViewSet, basename='permisos')
router.register(r'roles', RolViewSet, basename='roles')