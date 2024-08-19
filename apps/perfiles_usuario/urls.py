from django.urls import path, include

from .api.routers import router

app_name = 'perfiles_usuario'

urlpatterns = [
    path('', include(router.urls)),
]
