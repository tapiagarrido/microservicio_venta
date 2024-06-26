import uuid
from django.db import models
from vendedores.models import Vendedor

class Descuento(models.Model):
    nombre = models.CharField(max_length=100)
    tipo_descuento = models.CharField(max_length=20)
    porcentaje_descuento = models.DecimalField(max_digits=10, decimal_places=2)
    codigo_descuento = models.CharField(max_length=20, unique=True)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()

    def __str__(self):
        return self.nombre

class Venta(models.Model):
    fecha_venta = models.DateField()
    vendedor = models.ForeignKey(Vendedor,on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'Venta {self.id}'

class Venta_Detalle(models.Model):
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE)
    codigo_barra = models.CharField(max_length=20)
    cantidad = models.IntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)

