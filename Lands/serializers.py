from rest_framework import serializers
from .models import Land

class LandSerializer(serializers.ModelSerializer):
    propietario = serializers.ReadOnlyField(source='propietario.id')
    class Meta:
        model = Land
        fields = ['id', 'nombre', 'ubicacion', 'numero_cultivos', 'descripcion', 'propietario']
