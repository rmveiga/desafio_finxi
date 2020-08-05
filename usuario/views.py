from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

from.serializers import UsuarioSerializer


class UsuarioViewSet(viewsets.ModelViewSet):
    model = User
    serializer_class = UsuarioSerializer
    permission_classes = (AllowAny,)

    def create(self, request, *args, **kwargs):
        serializer = UsuarioSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            usuario = serializer.save()
            token = Token.objects.create(user=usuario)
            data.update({'response': 'Usuário registrado com sucesso'})
            data.update({'email': usuario.email})
            data.update({'username': usuario.username})
            data.update({'token': token.key})
        else:
            data = serializer.errors

        return Response(data, status=status.HTTP_201_CREATED)

    def get_queryset(self):
        return User.objects.all()
