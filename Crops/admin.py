from django.contrib import admin
from .models import Crop

@admin.register(Crop)
class CropAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'terreno', 'tipo', 'condicion_suelo_ideal', 'humedad_ideal', 'pa_ideal', 'calidad_luz_ideal', 'temperatura_ideal')
    search_fields = ('nombre', 'tipo', 'terreno__nombre')
