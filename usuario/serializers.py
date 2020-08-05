from rest_framework import serializers
from django.contrib.auth.models import User

class UsuarioSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    class Meta:
        model = User
        fields = [
            'email', 'username', 'password', 'password2'
        ]
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def save(self, **kwargs):
        usuario = User(
            email=self.validated_data.get('email'),
            username=self.validated_data.get('username'),
            is_staff=True
        )
        password = self.validated_data.get('password')
        password2 = self.validated_data.get('password2')

        if password != password2:
            raise serializers.ValidationError(
                {'password': 'As senhas informadas não conferem'}
            )

        usuario.set_password(password)
        usuario.save()

        return usuario