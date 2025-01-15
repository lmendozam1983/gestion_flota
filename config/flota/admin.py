from django.contrib import admin
from .models import User, Vehiculo, Asignacion

# Register your models here.

    
@admin.register(Vehiculo)
class VehiculoAdmin(admin.ModelAdmin):
    list_display = ('marca', 'modelo', 'patente', 'capacidad_carga', 'disponible')
    search_fields = ('marca', 'modelo', 'patente')
    list_filter = ('marca', 'disponible')
    ordering = ('marca', 'id')
    
@admin.register(Asignacion)
class AsignacionAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'vehiculo', 'fecha_asignacion', 'fecha_devolucion', 'estado')
    search_fields = ('usuario', 'vehiculo', 'estado')
    list_filter = ('usuario', 'vehiculo', 'estado')
    ordering = ('usuario', 'id')
    
    