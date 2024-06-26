from django.db import models
from django.conf import settings

class Land(models.Model):
    nombre = models.CharField(max_length=100)
    ubicacion = models.CharField(max_length=255)
    numero_cultivos = models.IntegerField(default=0)
    descripcion = models.TextField(blank=True, null=True)
    propietario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='lands')

    def __str__(self):
        return self.nombre
