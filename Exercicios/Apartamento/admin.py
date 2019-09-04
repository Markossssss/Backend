from django.contrib import admin

from .models import Apartamento

class ApartamentoAdmin(admin.ModelAdmin):
    list_display = (
        'numero',
        'qtdQuartos',
        'proprietario',
        'valorCondominio',
    )
admin.site.register(Apartamento,ApartamentoAdmin)

# Register your models here.
