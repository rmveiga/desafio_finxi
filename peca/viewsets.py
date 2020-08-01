from rest_framework import viewsets

from .models import Peca
from .serializers import PecaSerializer


class PecaViewSet(viewsets.ModelViewSet):
    queryset = Peca.objects.all()
    serializer_class = PecaSerializer
