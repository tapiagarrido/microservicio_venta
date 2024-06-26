from rest_framework import serializers
from vendedores.models import Vendedor

class VendedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendedor
        fields = ['id', 'nombre_completo', 'email','telefono','alias']

