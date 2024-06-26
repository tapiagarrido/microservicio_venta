from rest_framework import viewsets, response, status
from vendedores.models import Vendedor
from vendedores.api.serializer import VendedorSerializer

class VendedorViewSet(viewsets.ModelViewSet):

    queryset = Vendedor.objects.all()
    serializer_class = VendedorSerializer

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            respuesta = {
                "msg":"Vendedor registrado exitosamente",
                "vendedor": serializer.data
            }
            return response.Response(respuesta,status=status.HTTP_201_CREATED)
        
        return response.Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def list(self, request):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        vendedores_count = queryset.count()
        respuesta_vendedores={
            "total": vendedores_count,
            "vendedores": serializer.data,
            "msg": f"{vendedores_count} vendedores encontrados exitosamente"
        }
        return response.Response(respuesta_vendedores,status=status.HTTP_200_OK)
    
    def retrieve(self, request,pk=None):
        queryser = self.get_queryset().get(pk=pk)
        
    



