from rest_framework.routers import DefaultRouter
from ventas.api.views import VentaViewSet

router = DefaultRouter()

router.register('', VentaViewSet, basename='')
urlpatterns = router.urls