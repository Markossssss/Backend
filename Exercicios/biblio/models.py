from django.db import models

class Biblioteca(models.Model):
    titulo = models.CharField(max_length=10)
    autor = models.CharField(max_length=100)
    assunto = models.TextField()
    editora = models.CharField(max_length=50)
    ISBN = models.IntegerField()
    ano_publicacao = models.DateField()

class Autor(models.Model):
    class Meta:
        verbose_name_plural = "autores"
    nome = models.CharField(max_length=50)
    sobrenome = models.CharField(max_length=50)

    def __str__(self):
        return self.sobrenome.upper() + ','+ self.nome

class Aluno(models.Model):
    matricula = models.CharField('Matrícula', max_length=12, unique= True)
    nome = models.CharField('Nome',max_length=50)
    data_nascimento = models.DateField('Data de Nascimento')
    email = models.EmailField('E-mail', max_length=100)

    def __str__ (self):
        return self.nome

class Livro (models.Model):
    titulo = models.CharField('Título',max_length=100)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    ano_publicacao = models.IntegerField('Ano de Publicação')

    def __str__(self):
        return "{}, ({})".format(self.titulo, self.ano_publicacao)

class Emprestimo(models.Model):
    usuario = models.ForeignKey('auth.user', on_delete=models.CASCADE)
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    data_retirada = models.DateField()
    data_devolucao = models.DateField()
    livros = models.ManyToManyField(Livro)
    devolvido = models.BooleanField()



# Create your models here.
