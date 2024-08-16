from django.db import models

# Create your models here.

class GenericCatalogBaseClass(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(max_length=500, blank=True)

    class Meta:
        abstract = True
        ordering = ['id']

    def __str__(self):
        return self.nombre