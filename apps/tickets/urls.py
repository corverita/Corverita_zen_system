from django.urls import path, include

from .api.routers import router

app_name = 'tickets'

urlpatterns = [
    path('', include(router.urls)),
]
