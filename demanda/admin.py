from django.contrib import admin
from django.utils.html import format_html

from .models import Demanda


class DemandaAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'end_entrega', 'info_contato', 'peca', 'anunciante', 'status_img'
    ]

    def status_img(self, obj):
        img_true = '/img/baseline-check_circle_outline.svg'
        img_false = '/img/baseline-highlight_off.svg'
        if obj.status:
            return format_html(f'<img src="{img_true}"/>')
        else:
            return format_html(f'<img src="{img_false}"/>')

    status_img.allow_tags = True
    status_img.short_description = 'Status de Finalização'


admin.site.register(Demanda, DemandaAdmin)
