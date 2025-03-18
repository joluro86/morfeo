from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Vacante

@admin.register(Vacante)
class VacanteAdmin(admin.ModelAdmin):
    list_display = ('numero', 'nivel_academico')  # Muestra estos campos en la lista
    search_fields = ('numero',)  # Permite buscar por número de vacante
    list_filter = ('nivel_academico',)  # Agrega un filtro por nivel académico
