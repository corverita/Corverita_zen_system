from django.db import models
from django.core.validators import RegexValidator

from apps.usuarios.models import Usuario, Rol

# Create your models here.

class PerfilUsuario(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, related_name='perfil')
    biografia = models.TextField(max_length=500, blank=True)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    telefono = models.CharField(
        max_length=15,
        validators=[RegexValidator(regex=r'^\+?1?\d{9,15}$')],
        help_text="El número de teléfono debe estar en el formato: +999999999. Se permiten hasta 15 dígitos."
    )
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE, related_name='perfiles', null=True, blank=True, default=None)

    def __str__(self):
        return self.usuario.get_full_name()