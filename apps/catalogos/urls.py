from django.urls import path, include

from .api.routers import router

app_name = 'catalogos'

urlpatterns = [
    path('', include(router.urls)),
]
