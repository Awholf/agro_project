from django.db import models

class Crop(models.Model):
    nombre = models.CharField(max_length=100)
    terreno = models.OneToOneField('Lands.Land', on_delete=models.CASCADE, related_name='cultivo')
    tipo = models.CharField(max_length=50)
    condicion_suelo_ideal = models.CharField(max_length=255)
    humedad_ideal = models.CharField(max_length=50)
    pa_ideal = models.CharField(max_length=50)
    calidad_luz_ideal = models.IntegerField()
    temperatura_ideal = models.IntegerField()

    def __str__(self):
        return self.nombre
