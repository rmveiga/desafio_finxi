from rest_framework import serializers

from .models import Demanda


class DemandaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Demanda
        fields = [
            'end_entrega', 'info_contato', 'status', 'peca', 'anunciante'
        ]
