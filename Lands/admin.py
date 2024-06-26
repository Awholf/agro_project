from django.contrib import admin
from .models import Land

@admin.register(Land)
class LandAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'ubicacion', 'numero_cultivos', 'propietario')
    search_fields = ('nombre', 'ubicacion', 'propietario__username')
