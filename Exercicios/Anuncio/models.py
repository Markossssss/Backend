from django.db import models

class Anuncio(models.Model):
    cliente = models.CharField(max_length=50)
    textoTitulo = models.CharField(max_length=100)
    preco = models.FloatField()
    textoAnuncio = models.TextField(max_length=500)
    nomeContato = models.CharField(max_length=50)
    telefone = models.CharField(max_length=17)
    secao = models.CharField(max_length=50)
    tipoAnuncio = models.CharField(max_length=50)

    def __str__(self):
        return nome

# Create your models here.
