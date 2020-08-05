from rest_framework import routers
from .views import UsuarioViewSet

usuario_router = routers.DefaultRouter()
usuario_router.register('usuarios', UsuarioViewSet, basename='usuario-registro')