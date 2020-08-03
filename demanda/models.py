from django.db import models
from django.contrib.auth.models import User

from peca.models import Peca

class Demanda(models.Model):
    end_entrega = models.CharField(max_length=100, verbose_name='Endereço de Entrega')
    info_contato = models.CharField(max_length=50, verbose_name='Informações de Contato')
    status = models.BooleanField(default=False, verbose_name='Status de Finalização')
    peca = models.ForeignKey(Peca, on_delete=models.DO_NOTHING, verbose_name='Peça')
    anunciante = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name='Anunciante')

    def __str__(self):
        return f'id: {str(self.pk)} - {str(self.peca)} - {str(self.anunciante)} - status: {str(self.status)}'

    # def status_img(self):
    #     self.img_true = r'img/baseline-check_circle_outline.svg'
    #     self.img_false = r'img/baseline-highlight_off.svg'
    #     if self.status:
    #         return r'<img src="%s"/>' % self.img_true
    #     else:
    #         return '<img src="{self.img_false}"/>'
    #
    # status_img.allow_tags = True
    # status_img.short_description = 'Status de Finalização'