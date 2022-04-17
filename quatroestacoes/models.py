from django.db import models


class Morador(models.Model):
    nome = models.CharField(max_length=50)
    sobrenome = models.CharField(max_length=50)

    opcoes_bloco = [
        ("A", "A"),
        ("B", "B"),
        ("C", "C"),
        ("D", "D"),
    ]
    bloco = models.CharField(max_length=50, choices=opcoes_bloco)

    opcoes_apartamento = [
        (1, "01"),
        (2, "02"),
        (11, "11"),
        (12, "12"),
        (21, "21"),
        (22, "22"),
        (31, "31"),
        (32, "32"),
    ]
    apartamento = models.IntegerField(choices=opcoes_apartamento)
    
    interfone = models.IntegerField()
    celular = models.IntegerField()
    email = models.EmailField()
    sindico = models.BooleanField(verbose_name="É síndico?")
    usuario_criado = models.BooleanField(editable=False, default=False)

    class Meta:
        verbose_name_plural = "Moradores"


class Reserva(models.Model):
    morador = models.ForeignKey(Morador, on_delete=models.CASCADE, verbose_name="ID do morador")
    data = models.DateField()


class Reuniao(models.Model):
    data = models.DateTimeField(verbose_name="Data e horário da reunião")
    assunto = models.CharField(max_length=300)

    class Meta:
        verbose_name_plural = "Reunioes"


class Aviso(models.Model):
    assunto = models.CharField(max_length=300)
    corpo = models.TextField()
    data_postagem = models.DateTimeField(auto_now_add=True)
    data_evento = models.DateTimeField(blank=True, null=True)


class Reclamacao(models.Model):
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


if __name__ == "__main__":
    pass