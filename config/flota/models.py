from django.db import models
from django.contrib.auth.models import User

# Create your models here.
    
class Vehiculo(models.Model):
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    patente = models.CharField(max_length=100, unique=True)
    capacidad_carga = models.DecimalField(max_digits=10, decimal_places=2)
    disponible = models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.marca} - {self.modelo} - {self.patente}"
    
class Asignacion(models.Model):
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_asignacion = models.DateField(auto_now_add=True)
    fecha_devolucion = models.DateField(auto_now=True)
    estado = models.CharField(
        choices=[('Activa', 'activa'), ('Completada', 'completada'), ('Cancelada', 'cancelada')],
        max_length=50
    )
    
    def __str__(self):
        return f"{self.vehiculo} - {self.usuario}"
    
    