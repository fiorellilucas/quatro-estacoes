from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


class MoradorManager(BaseUserManager):

    def create_user(self, email, password, bloco, apartamento, interfone, celular, **extra_fields):

        if not email:
            raise ValueError("O email não pode ficar em branco")
        if not bloco:
            raise ValueError("O bloco não pode ficar em branco")
        if not apartamento:
            raise ValueError("O apartamento não pode ficar em branco")
        if not interfone:
            raise ValueError("O interfone não pode ficar em branco")
        if not celular:
            raise ValueError("O celular não pode ficar em branco")

        usuario = self.model(
            email=self.normalize_email(email),
            password=password,
            bloco=bloco,
            apartamento=apartamento,
            interfone=interfone,
            celular=celular,
            **extra_fields
        )
        usuario.set_password(password)
        usuario.save(using=self._db)
        return usuario

    def create_superuser(self, email, password, bloco, apartamento, interfone, celular, **extra_fields):

        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        usuario = self.create_user(
            email=self.normalize_email(email),
            password=password,
            bloco=bloco,
            apartamento=apartamento,
            interfone=interfone,
            celular=celular,
            **extra_fields
        )
        return usuario


class Morador(AbstractUser):

    username = None
    email = models.EmailField(unique=True)
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

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ["password", "bloco",
                       "apartamento", "interfone", "celular"]

    objects = MoradorManager()

    def __str__(self):
        return self.email

    class Meta:
        verbose_name_plural = "Moradores"


class Reserva(models.Model):

    morador = models.ForeignKey(
        Morador, on_delete=models.CASCADE, verbose_name="ID do morador")
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
