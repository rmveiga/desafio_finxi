from rest_framework import serializers

from .models import Peca


class PecaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Peca
        fields = ['descricao', 'usuario']
