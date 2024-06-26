from rest_framework import viewsets, permissions
from .models import Crop
from .serializers import CropSerializer
from Lands.models import Land 
from rest_framework.exceptions import ValidationError

class CropViewSet(viewsets.ModelViewSet):
    queryset = Crop.objects.all()
    serializer_class = CropSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        user = self.request.user
        try:
            # Suponiendo que cada usuario tiene un terreno único
            terreno = Land.objects.get(propietario=user)
        except Land.DoesNotExist:
            raise ValidationError('No se encontró un terreno para el usuario autenticado.')
        
        serializer.save(terreno=terreno)