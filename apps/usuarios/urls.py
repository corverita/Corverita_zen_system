from django.urls import path, include

from .api.routers import router
from .api.views import RegistroUsuario, LoginView

app_name = 'usuarios'

urlpatterns = [
    path('usuarios/', include(router.urls)),
    path('usuarios/registro/', RegistroUsuario.as_view(), name='registro'),
    path('usuarios/login/', LoginView.as_view(), name='login'),
]
