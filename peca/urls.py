from rest_framework import routers

from .viewsets import PecaViewSet

peca_router = routers.DefaultRouter()
peca_router.register('pecas', PecaViewSet)