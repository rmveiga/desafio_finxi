from django.db import models
from django.contrib.auth.models import User

class Peca(models.Model):
    descricao = models.CharField(max_length=100, verbose_name='Descrição')
    usuario = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.descricao
