from .models import Morador
from django.forms import ModelForm
from django.contrib.auth.models import User


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

        Morador.objects.create(
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
        model = Morador
        fields = "__all__"


