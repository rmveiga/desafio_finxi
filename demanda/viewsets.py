from rest_framework import viewsets
from rest_framework.response import Response

from .models import Demanda
from .serializers import DemandaSerializer


class DemandaViewSet(viewsets.ModelViewSet):
    def list(self, request, *args, **kwargs):
        usuario = request.user
        if usuario.is_superuser:
            queryset = Demanda.objects.all()
        elif usuario.is_staff:
            queryset = Demanda.objects.filter(anunciante=usuario)
        else:
            return Response({'Acesso negado': 'Você não têm permissão para visualizar estes dados'})

        serializer = DemandaSerializer(queryset, many=True)
        return Response(serializer.data)
