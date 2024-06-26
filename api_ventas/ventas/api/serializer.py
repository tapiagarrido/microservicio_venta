from rest_framework import serializers
from ventas.models import Vendedor, Descuento, Venta, Venta_Detalle

class VendedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendedor
        fields = ['id', 'nombre_completo', 'email']

class DescuentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Descuento
        fields = ['id', 'nombre', 'tipo_descuento', 'porcentaje_descuento', 'codigo_descuento', 'fecha_inicio', 'fecha_fin']

class VentaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venta
        fields = ['id', 'fecha_venta', 'vendedor']

class VentaDetalleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venta_Detalle
        fields = ['id', 'venta', 'codigo_barra', 'cantidad', 'precio_unitario']

class VentaConDetalleSerializer(serializers.ModelSerializer):
    detalles = VentaDetalleSerializer(many=True, read_only=True)

    class Meta:
        model = Venta
        fields = ['id', 'fecha_venta', 'vendedor', 'detalles']