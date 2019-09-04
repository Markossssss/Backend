from django.contrib import admin

from .models import Anuncio

class AnuncioAdmin(admin.ModelAdmin):
    list_display = ('textoTitulo','textoAnuncio','preco','telefone','tipoAnuncio')

admin.site.register(Anuncio,AnuncioAdmin)

# Register your models here.
