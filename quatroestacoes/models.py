from django.db import models


class Morador(models.Model):
    id_morador = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=50)
    sobrenome = models.CharField(max_length=50)
    bloco = models.CharField(max_length=50)
    apartamento = models.IntegerField()
    interfone = models.IntegerField()
    celular = models.IntegerField()
    email = models.EmailField()
    sindico = models.BooleanField(verbose_name="É síndico?")


    class Meta:
        verbose_name_plural = "Moradores"


class Reserva(models.Model):
    id_reserva = models.AutoField(primary_key=True)
    morador = models.ForeignKey(Morador, on_delete=models.CASCADE, verbose_name="ID do morador")
    data = models.DateField()


class Reuniao(models.Model):
    id_reuniao = models.AutoField(primary_key=True)
    data = models.DateTimeField(verbose_name="Data e horário da reunião")
    assunto = models.CharField(max_length=300)


    class Meta:
        verbose_name_plural = "Reunioes"


class Aviso(models.Model):
    id_aviso = models.AutoField(primary_key=True)
    assunto = models.CharField(max_length=300)
    corpo = models.TextField()
    data_postagem = models.DateTimeField(auto_now_add=True)
    data_evento = models.DateTimeField(blank=True, null=True)


class Reclamacao(models.Model):
    id_reclamacao = models.AutoField(primary_key=True)
    morador = models.ForeignKey(Morador, on_delete=models.CASCADE, verbose_name="ID do morador")
    
    RECLAMACAO = "reclamacao"
    SUGESTAO = "sugestao"
    opcoes = [
        (RECLAMACAO, "Reclamação"),
        (SUGESTAO, "Sugestão"),
    ]    
    
    tipo = models.CharField(choices=opcoes, max_length=50)
    assunto = models.CharField(max_length=300)
    corpo = models.TextField()
    data_postagem = models.DateTimeField(auto_now_add=True)


    class Meta:
        verbose_name_plural = "Reclamacoes"


