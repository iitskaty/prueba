from django.db import models
from django.utils import timezone

class Visitas(models.Model):
    nombre = models.CharField(max_length=100)
    rut = models.CharField(max_length=12, unique=True)
    descripcion = models.CharField(max_length=256,default="")
    hora_ingreso = models.DateTimeField(db_default=timezone ,auto_now_add=False)
    hora_salida = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.nombre} - {self.rut}"