from rest_framework import serializers
from .models import Crop

class CropSerializer(serializers.ModelSerializer):
    class Meta:
        model = Crop
        fields = ['id', 'nombre', 'terreno', 'tipo', 'condicion_suelo_ideal', 'humedad_ideal', 'pa_ideal', 'calidad_luz_ideal', 'temperatura_ideal']
        extra_kwargs = {
            'terreno': {'required': False}
        }