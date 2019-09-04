from django.contrib import admin

from .models import Despesas
class DespesasAdmin(admin.ModelAdmin):
    list_display = ('descricao','vencimento','quitado')
admin.site.register(Despesas,DespesasAdmin)

# Register your models here.
