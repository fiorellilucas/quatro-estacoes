from django.urls import path
from . import views

app_name = "quatroestacoes"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    
    #TODO: moradores/ (alterar, deletar)
    #TODO: reunioes/ (alterar, deletar)
    #TODO: reclamacoes/
    #TODO: reservas/
    #TODO: avisos/

    #TODO: usar template da Samira, user auth, area do morador

    path("login/", views.LoginView.as_view(), name="login"),  #TODO: Redirecionar todas as páginas para login/ se não estiver logado
    path("admin/", views.AdminView.as_view(), name="admin"),
    path("admin/moradores", views.MoradorView.as_view(), name="moradores_admin"),
    path("admin/moradores/adicionar", views.MoradorAddView.as_view(), name="morador_add"),
    path("admin/reunioes", views.ReuniaoView.as_view(), name="reuniao_admin"),
    path("admin/reunioes/adicionar", views.ReuniaoAddView.as_view(), name="reuniao_add"),
    path("admin/reclamacoes", views.ReclamacaoView.as_view(), name="reclamacao_admin"),
    path("admin/reclamacoes/adicionar", views.ReclamacaoAddView.as_view(), name="reclamacao_add"),
    path("admin/avisos", views.AvisoView.as_view(), name="aviso_admin"),
    path("admin/avisos/adicionar", views.AvisoAddView.as_view(), name="aviso_add"),
]