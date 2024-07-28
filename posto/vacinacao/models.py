from django.db import models

# Create your models here.
class Crianca(models.Model):
    nome_crianca = models.CharField(max_length=100)
    idade_crianca = models.IntegerField()
    nome_mae = models.CharField(max_length=100)
    vacina = models.CharField(max_length=100, blank=True)
    bairro = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nome_crianca} ({self.nome_mae} / {self.vacina})"
