from django.db import models

class Biblioteca(models.Model):
    titulo = models.CharField(max_length=10)
    autor = models.CharField(max_length=100)
    assunto = models.TextField()
    editora = models.CharField(max_length=50)
    ISBN = models.IntegerField()
    ano_publicacao = models.DateField()

# Create your models here.
