from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action

from .models import Demanda
from .serializers import DemandaSerializer


class DemandaViewSet(viewsets.ModelViewSet):
    model = Demanda
    serializer_class = DemandaSerializer

    @action(detail=True, methods=['post'])
    def finalizar_demanda(self, request, pk=None):
        usuario = request.user
        if not usuario.is_staff and not usuario.is_superuser:
            return Response({'Acesso negado': 'Você não têm permissão para finalizar demandas'})

        try:
            demanda = Demanda.objects.get(pk=pk)
        except Exception:
            return Response({'Aviso': 'Demanda não encontrada'})

        if usuario != demanda.anunciante:
            return Response({'Acesso negado': 'Você não têm permissão para finalizar esta demanda'})
        if demanda.status:
            return Response({'Aviso': 'Esta demanda já está finalizada'})
        else:
            instance = demanda
            serializer = self.get_serializer(instance, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.validated_data.update({'status': True})
            self.perform_update(serializer)

            return Response(serializer.data)

    def list(self, request, *args, **kwargs):
        usuario = request.user
        if usuario.is_superuser:
            queryset = Demanda.objects.all()
        elif usuario.is_staff:
            queryset = Demanda.objects.filter(anunciante=usuario)
        else:
            return Response({'Acesso negado': 'Você não têm permissão para visualizar demandas'})

        serializer = DemandaSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        usuario = request.user
        if not usuario.is_staff and not usuario.is_superuser:
            return Response({'Acesso negado': 'Você não têm permissão para visualizar demandas'})

        try:
            demanda = Demanda.objects.get(pk=kwargs.get('pk'))
        except Exception:
            return Response({'Aviso': 'Demanda não encontrada'})

        if usuario != demanda.anunciante:
            return Response({'Acesso negado': 'Você não têm permissão para visualizar esta demanda'})
        else:
            instance = demanda
            serializer = self.get_serializer(instance)

            return Response(serializer.data)

    def perform_create(self, serializer):
        usuario = self.request.user
        serializer.validated_data.update({'anunciante': usuario})
        serializer.save()

    def create(self, request, *args, **kwargs):
        usuario = request.user
        if not usuario.is_staff and not usuario.is_superuser:
            return Response({'Acesso negado': 'Você não têm permissão para cadastrar demandas'})
        else:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)

            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def update(self, request, *args, **kwargs):
        usuario = request.user
        if not usuario.is_staff and not usuario.is_superuser:
            return Response({'Acesso negado': 'Você não têm permissão para alterar demandas'})

        try:
            demanda = Demanda.objects.get(pk=kwargs.get('pk'))
        except Exception:
            return Response({'Aviso': 'Demanda não encontrada'})

        if usuario != demanda.anunciante:
            return Response({'Acesso negado': 'Você não têm permissão para alterar esta demanda'})
        else:
            partial = kwargs.pop('partial', False)
            instance = demanda
            serializer = self.get_serializer(instance, data=request.data, partial=partial)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)

            return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        usuario = request.user
        if not usuario.is_staff and not usuario.is_superuser:
            return Response({'Acesso negado': 'Você não têm permissão para excluir demandas'})

        try:
            demanda = Demanda.objects.get(pk=kwargs.get('pk'))
        except Exception:
            return Response({'Aviso': 'Demanda não encontrada'})

        if usuario != demanda.anunciante:
            return Response({'Acesso negado': 'Você não têm permissão para excluir esta demanda'})
        else:
            instance = demanda
            self.perform_destroy(instance)

            return Response(
                {'Aviso': 'Demanda excluída com sucesso'},
                status=status.HTTP_204_NO_CONTENT
            )