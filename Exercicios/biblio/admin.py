from django.contrib import admin

from .models import Biblioteca

class BibliotecaAdmin(admin.ModelAdmin):
    list_display = ('autor', 'titulo', 'autor')

admin.site.register(Biblioteca,BibliotecaAdmin)


# Register your models here.
