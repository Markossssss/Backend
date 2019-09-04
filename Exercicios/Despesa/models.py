from django.db import models

class Despesas(models.Model):
    data_criacao = models.CharField
    descricao = models.TextField(max_length=500)
    vencimento = models.DateField(max_length=50)
    quitado = models.BooleanField
    forma_pagamento_CHOICES = (
        ('Boleto', 'Boleto'),
        ('Cheque','Cheque'),
        ('Crédito','Crédito'),
        ('Débito', 'Débito'),
        ('Dinheiro', 'Dinheiro'),
    )
    tipo_despesa_CHOICES = (
        ('Boleto de cobrança', 'Boleto de cobrança'),
        ('Conta de energia', 'Conta de energia'),
        ('Conta de água','Conta de água'),
        ('Telefonia','Telefonia'),
        ('Outro','Outro'),
    )
    tipo_despesa = models.CharField(max_length=100, choices=tipo_despesa_CHOICES)
    forma_pagamento = models.CharField(max_length=100,choices=forma_pagamento_CHOICES)
# Create your models here.
