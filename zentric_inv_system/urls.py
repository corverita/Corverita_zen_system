from django.contrib import admin
from django.urls import path
from django.urls.conf import include

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="API Zentric",
        default_version='v1',
        description="API del sistema de inventario de Zentric",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="oscar.corvera@live.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('apps.usuarios.urls')), # Incluye las rutas de la app usuarios
    path('api/v1/', include('apps.perfiles_usuario.urls')), # Incluye las rutas de la app perfiles_usuario
    path('api/v1/', include('apps.catalogos.urls')), # Incluye las rutas de la app catalogos
    path('api/v1/', include('apps.productos.urls')), # Incluye las rutas de la app productos
#     path('api/v1/', include('apps.tickets.urls')), # Incluye las rutas de la app tickets


    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),  # Registra el nombre de espacio 'rest_framework' para las rutas de autenticación

    # Path API Swagger
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('swagger/api/v1/user/login/', schema_view.with_ui('swagger', cache_timeout=0), name='rest_framework_login'),
    path('swagger/api/v1/user/logout/', schema_view.with_ui('swagger', cache_timeout=0), name='rest_framework_logout'),
]
