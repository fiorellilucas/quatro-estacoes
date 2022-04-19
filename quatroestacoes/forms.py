from . import models
from django.forms import ModelForm
from django.contrib.auth.models import User
from django import forms


class MoradorForm(ModelForm):
     
    def adicionar_morador(self):
        morador = self.cleaned_data

        nome = morador.get("nome")
        sobrenome = morador.get("sobrenome")
        bloco = morador.get("bloco")
        apartamento = morador.get("apartamento")
        interfone = morador.get("interfone")
        celular = morador.get("celular")
        email = morador.get("email")
        sindico = morador.get("sindico")

        models.Morador.objects.create(
            nome=nome,
            sobrenome=sobrenome,
            bloco=bloco,
            apartamento=apartamento,
            interfone=interfone,
            celular=celular,
            email=email,
            sindico=sindico
        )

    def criar_usuario(self):
        morador = self.cleaned_data

        nome = morador.get("nome").lower()
        sobrenome = morador.get("sobrenome").lower()
        email = morador.get("email")

        User.objects.create_user(
            username=f"{nome}{sobrenome}",
            password="123abc",
            email=email,
            first_name=nome,
            last_name=sobrenome,
        )

    class Meta:
        model = models.Morador
        fields = "__all__"


class ReuniaoForm(ModelForm):

    def criar_reuniao(self):
        reuniao = self.cleaned_data

        data = reuniao.get("data")
        assunto = reuniao.get("assunto")

        models.Reuniao.objects.create(
            data=data,
            assunto=assunto
        )
    
    class Meta:
        model = models.Reuniao
        fields = "__all__"
        widgets = {
            "data": forms.DateTimeInput(attrs={"type": "datetime-local"}),
        }


class ReclamacaoForm(ModelForm):
    
    def criar_reclamacao(self):
        reclamacao = self.cleaned_data
        
        tipo = reclamacao.get("tipo")
        assunto = reclamacao.get("assunto")
        corpo = reclamacao.get("corpo")

        models.Reclamacao.objects.create(
            tipo=tipo,
            assunto=assunto,
            corpo=corpo,
        )

    class Meta:
        model = models.Reclamacao
        fields = "__all__"


class AvisoForm(ModelForm):

    def criar_aviso(self):
        aviso = self.cleaned_data

        assunto = aviso.get("assunto")
        corpo = aviso.get("corpo")
        data_evento = aviso.get("data_evento")

        models.Aviso.objects.create(
            assunto=assunto,
            corpo=corpo,
            data_evento=data_evento,
        )

    class Meta:
        model = models.Aviso
        fields = "__all__"
        widgets = {
            "data_evento": forms.DateTimeInput(attrs={"type": "datetime-local"}),
        }

