from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from apps.usuarios.models import Usuario

# Create your models here.

class PerfilUsuario(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, related_name='perfil')
    biografia = models.TextField(max_length=500, blank=True)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    telefono = models.IntegerField(blank=True, validators=[MinValueValidator(1000000000), MaxValueValidator(9999999999)])

    def __str__(self):
        return self.usuario.get_full_name()