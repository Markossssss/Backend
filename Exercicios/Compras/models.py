from django.db import models

class Compras(models.Model):
    nome = models.CharField(max_length=100)
    descricaoProduto = models.TextField(max_length=500)
    unidadeCompra = models.CharField(max_length=10)
    qtdPrevistoMes = models.FloatField()
    preco = models.FloatField()
    precoMaximo = models.FloatField()

    def __str__(self):
        return self.nome
# Create your models here.
