from django.db import models

# Create your models here.

class Balconista(models.Model): 
    nome_usuario = models.CharField(max_length=100)
    senha = models.IntegerField()
    nivelacesso = models.IntegerField()
    