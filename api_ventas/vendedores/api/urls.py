from rest_framework.routers import DefaultRouter
from vendedores.api.views import VendedorViewSet

router = DefaultRouter()

router.register('', VendedorViewSet, basename='')
urlpatterns = router.urls