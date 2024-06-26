from django.db import models

class Vendedor(models.Model):
    email = models.EmailField(primary_key=True)  
    nombre_completo = models.CharField(max_length=200)
    telefono = models.CharField(max_length=25, null=True)
    alias = models.CharField(max_length=50, default='')

    def __str__(self):
        return f'Vendedor {self.email}'
