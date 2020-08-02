from rest_framework import routers

from .viewsets import DemandaViewSet

demanda_router = routers.DefaultRouter()
demanda_router.register('demandas', DemandaViewSet, basename='demanda-list')