from rest_framework import routers
from pruebaTec.api import productoViewSet

router = routers.DefaultRouter()

router.register('api/productos', productoViewSet, 'producto')

urlpatterns = router.urls