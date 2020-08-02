from rest_framework import viewsets
from rest_framework.response import Response

from .models import Demanda
from .serializers import DemandaSerializer


class DemandaViewSet(viewsets.ModelViewSet):
    model = Demanda
    serializer_class = DemandaSerializer

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

    def perform_create(self, serializer):
        usuario = self.request.user
        serializer.validated_data.update({'anunciante': usuario})
        serializer.save()

