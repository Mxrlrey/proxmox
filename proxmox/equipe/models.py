from django.db import models

class Equipe(models.Model):
    nome = models.CharField("Nome da equipe", max_length=100, unique=True)
    usuario = models.CharField("Nome do usuário que utilizou para seguir a apresentação", max_length=100)
    membro1 = models.CharField("Membro 1", max_length=100)
    membro2 = models.CharField("Membro 2", max_length=100, blank=True, null=True)

    def __str__(self):
        return self.nome
