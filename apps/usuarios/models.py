from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Permiso(models.Model):
    nombre = models.CharField(max_length=50, unique=True, verbose_name='Nombre del permiso')

    def __str__(self):
        return self.nombre
    
    class Meta:
        ordering = ['id']
        verbose_name = 'Permiso'
        verbose_name_plural = 'Permisos'

class Rol(models.Model):
    nombre = models.CharField(max_length=50, unique=True, verbose_name='Nombre del rol')
    permisos = models.ManyToManyField(Permiso, verbose_name='Permisos')

    def __str__(self):
        return self.nombre
    
    class Meta:
        ordering = ['id']
        verbose_name = 'Rol'
        verbose_name_plural = 'Roles'

class Usuario(AbstractUser):
    email = models.EmailField(unique=True, verbose_name='Correo electrónico')

    def __str__(self):
        return self.get_full_name()