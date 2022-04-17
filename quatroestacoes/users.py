from django.contrib.auth.models import User
from .models import Morador
from django.db.utils import IntegrityError

def criar_usuario():
    moradores_sem_usuario = Morador.objects.all().filter(usuario_criado=False)
    for morador in moradores_sem_usuario:
        SENHA = "123abc"
        try:
            novo_usuario = User.objects.create_user(
                username = f"{morador.nome.lower()}{morador.sobrenome.lower()}",
                email = morador.email,
                password = SENHA
            )
            novo_usuario.groups.add("Morador")
        except IntegrityError:
            pass
        
        #TODO: Criar padrão para senha
        #TODO: Criar grupo "Moradores" e adicionar "novo_usuario"

if __name__ == "__main__":
    pass