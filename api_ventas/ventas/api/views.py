from rest_framework import viewsets, response, status, pagination
from ventas.models import Venta
from ventas.api.serializer import VentaConDetalleSerializer, VentaDetalleSerializer

class VentaPagination(pagination.PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 1000

class VentaViewSet(viewsets.ModelViewSet):

    queryset = Venta.objects.all().order_by('-id')
    serializer_class = VentaConDetalleSerializer

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            venta = serializer.save()
            detalles_data = request.data.get('detalles', [])
            detalles_guardados = []
            for detalle_data in detalles_data:
                detalle_data['venta'] = venta.id
                venta_detalle_serializer = VentaDetalleSerializer(data=detalle_data)
                if venta_detalle_serializer.is_valid():
                    venta_detalle_serializer.save()
                    detalles_guardados.append(venta_detalle_serializer.data)
                else:
                    venta.delete()
                    return response.Response(venta_detalle_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            venta_actualizada = Venta.objects.get(id=venta.id)
            serializer = self.get_serializer(venta_actualizada)
            serializer_data = serializer.data
            serializer_data['detalles'] = detalles_guardados
            return response.Response(serializer_data, status=status.HTTP_201_CREATED)
        else:
            return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request):
        paginator = VentaPagination()
        queryset = self.get_queryset()
        result_page = paginator.paginate_queryset(queryset,request)
        serializer = self.get_serializer(result_page, many=True)
        ventas_count = queryset.count()
        mensaje = {"msg": f"{len(serializer.data)} ventas han sido encontradas exitosamente"}
        total_ventas = {"total de registros": ventas_count}
        data_ventas = {"ventas": serializer.data, **total_ventas, **mensaje}
        return response.Response(data_ventas, status=status.HTTP_200_OK)
    
    def retrieve(self, request, pk=None):
        try:
            venta = self.get_queryset().get(pk=pk)
            serializer = self.get_serializer(venta)
            detalles_venta = VentaDetalleSerializer(venta.venta_detalle_set.all(), many=True).data
            serializer_data = serializer.data
            serializer_data['detalles'] = detalles_venta
            mensaje = {"msg": f"Venta {pk} ha sido encontrada exitosamente"}
            data_venta_id = {"Venta":serializer_data, **mensaje }
            return response.Response(data_venta_id, status=status.HTTP_200_OK)
        except Venta.DoesNotExist:
            return response.Response({"error": "La venta indicada no existe"}, status=status.HTTP_404_NOT_FOUND)
