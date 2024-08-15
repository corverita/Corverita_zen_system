from django.contrib import admin

# Register your models here.

from .models import Estatus, Prioridad, TipoMovimiento

admin.site.register(Estatus)
admin.site.register(Prioridad)
admin.site.register(TipoMovimiento)