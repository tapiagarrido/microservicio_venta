import jwt 
from django.http import JsonResponse
from django.conf import settings
from rest_framework import status
from django.utils.deprecation import MiddlewareMixin
from vendedores.models import Vendedor

class JWTAuthenticationMiddleware(MiddlewareMixin):
    def process_request(self,request):
        auth_header = request.headers.get('Authorization')
        
        if not auth_header or not auth_header.startswith('Bearer '):
            return JsonResponse({"error": "Token con formato invalido o no existe"},status=status.HTTP_403_FORBIDDEN)
        
        token = auth_header.split(' ')[1]

        try:
            payload = jwt.decode(token, settings.JWT_SEED, algorithms=["HS256"])
        except jwt.ExpiredSignatureError:
            return JsonResponse({"error": "El token ha expirado"},status=status.HTTP_403_FORBIDDEN)
        except jwt.InvalidTokenError:
            return JsonResponse({"Error":"Token invalido"},status=status.HTTP_403_FORBIDDEN)
        
        email = payload.get('email')
        nombre_completo = payload.get('nombre_completo')
        telefono = payload.get('telefono')
        alias = payload.get('alias')

        try:
            vendedor_existe = Vendedor.objects.get(email=email)
        except Vendedor.DoesNotExist:
            registro_vendedor = Vendedor(email=email,nombre_completo=nombre_completo,telefono=telefono, alias=alias)
            registro_vendedor.save()

        request.email = email
        request.nombre_completo = nombre_completo
        request.telefono = telefono
        request.alias = alias

        return None