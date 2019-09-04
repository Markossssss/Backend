from django.db import models

class Apartamento(models.Model):
    numero = models.IntegerField()
    qtdQuartos = models.IntegerField()
    proprietario = models.CharField(max_length=50)
    valorCondominio = models.FloatField()

    def __str__(self):
        return self.nome

# Create your models here.
