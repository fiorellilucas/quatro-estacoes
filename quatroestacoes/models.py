from django.db import models

class Moradores(models.Model):
    id_morador = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=50)
    sobrenome = models.CharField(max_length=50)
    bloco = models.CharField(max_length=50)
    apartamento = models.IntegerField()
    interfone = models.IntegerField()
    celular = models.IntegerField()
    email = models.EmailField()
    sindico = models.BooleanField()
