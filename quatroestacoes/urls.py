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
    path("admin/moradores", views.MoradoresListaView.as_view(), name="morador_admin"),
    path("admin/moradores/<int:id_morador>", views.MoradoresInfoView.as_view(), name="moradores_info"),
    path("admin/moradores/adicionar", views.MoradoresAddView.as_view(), name="morador_add"),
    path("admin/moradores/<int:pk>/alterar", views.MoradoresUpdView.as_view(), name="moradores_upd"),
    path("admin/moradores/<int:pk>/deletar", views.MoradoresDelView.as_view(), name="moradores_del"),
    path("admin/reunioes", views.ReunioesListaView.as_view(), name="reuniao_admin"),
    path("admin/reunioes/adicionar", views.ReunioesAddView.as_view(), name="reuniao_add"),
    path("admin/reclamacoes", views.ReclamacoesListaView.as_view(), name="reclamacao_admin"),
    path("admin/reclamacoes/adicionar", views.ReclamacoesAddView.as_view(), name="reclamacao_add"),
    path("admin/avisos", views.AvisosListaView.as_view(), name="aviso_admin"),
    path("admin/avisos/adicionar", views.AvisosAddView.as_view(), name="aviso_add"),
]
