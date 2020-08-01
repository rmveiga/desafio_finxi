from django.db import models


class Peca(models.Model):
    descricao = models.CharField(max_length=100, verbose_name='Descrição')

    def __str__(self):
        return self.descricao
