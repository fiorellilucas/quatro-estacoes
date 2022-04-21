from django.forms import ModelForm
from django.contrib.auth.models import User
from django import forms

from . import models

class MoradorForm(ModelForm):

    def criar_usuario(self):
        morador = self.cleaned_data

        nome = morador.get("nome")
        sobrenome = morador.get("sobrenome")
        username = f"{nome.lower().split()[0]}{sobrenome.lower().split()[0]}"
        email = morador.get("email")

        User.objects.create_user(
            username=username,
            password="123abc",
            email=email,
            first_name=nome,
            last_name=sobrenome,
        )

    class Meta:
        model = models.Morador
        fields = "__all__"


class ReuniaoForm(ModelForm):
    
    class Meta:
        model = models.Reuniao
        fields = "__all__"
        widgets = {
            "data": forms.DateTimeInput(attrs={"type": "datetime-local"}),
        }


class ReclamacaoForm(ModelForm):

    class Meta:
        model = models.Reclamacao
        fields = "__all__"


class AvisoForm(ModelForm):

    class Meta:
        model = models.Aviso
        fields = "__all__"
        widgets = {
            "data_evento": forms.DateTimeInput(attrs={"type": "datetime-local"}),
        }

