from django.db import models

from apps.catalogos.models import Estatus, Prioridad
from apps.usuarios.models import Usuario

# Create your models here.

class Ticket(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=500)
    estatus = models.ForeignKey(Estatus, on_delete=models.CASCADE)
    prioridad = models.ForeignKey(Prioridad, on_delete=models.CASCADE, null=True, blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True)

    class Meta:
        ordering = ['id']

class Comentario(models.Model):
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    comentario = models.TextField(max_length=500)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True)

    class Meta:
        ordering = ['id']