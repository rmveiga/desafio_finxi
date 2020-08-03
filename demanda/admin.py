from django.contrib import admin

from .models import Demanda

class DemandaAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'end_entrega', 'info_contato', 'status', 'peca', 'anunciante'
    ]


admin.site.register(Demanda, DemandaAdmin)
