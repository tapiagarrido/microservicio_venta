from django.http import JsonResponse
from django.conf import settings

class SecurityHeaderMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        secret_key = request.headers.get('X-Secret')

        if secret_key != settings.X_SECRET_ESPERADO:
            return JsonResponse({"error": "No está autorizado a usar el servicio"}, status=403)
        
        return self.get_response(request)
