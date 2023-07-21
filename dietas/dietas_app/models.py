from django.db import models

class Base(models.Model):
    criados = models.DateField('Criação', auto_now_add=True)
    modificado = models.DateField('Atualização', auto_now=True)
    ativo = models.BooleanField('Ativo?', default=True )

    class Meta:
        abstract = True

class Paciente(Base):
    nome = models.CharField('nome', max_length=100)
    telefone = models.CharField('Telefone', max_length=20)
    email = models.EmailField('E-mail')

    def _str_(self) -> str:
        return self.nome
