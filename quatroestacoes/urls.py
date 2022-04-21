from django.urls import path

from . import views

#TODO: usar template da Samira, user auth, area do morador

app_name = "quatroestacoes"
urlpatterns = [
    # USUÁRIO COMUM
    path("", views.IndexView.as_view(), name="index"),
    path("moradores/", views.MoradoresListaView.as_view(), name="moradores_lista"),
    path("moradores/<int:id_morador>/", views.MoradoresInfoView.as_view(), name="moradores_info"),
    path("avisos/", views.AvisosListaView.as_view(), name="avisos_lista"),
    path("reclamacoes/", views.ReclamacoesListaView.as_view(), name="reclamacoes_lista"),
    path("login/", views.LoginView.as_view(), name="login"),  #TODO: Redirecionar todas as páginas para login/ se não estiver logado
    
    # ADMIN
    path("admin/", views.AdminIndexView.as_view(), name="index_admin"),
    path("admin/moradores/", views.MoradoresListaView.as_view(), name="moradores_lista_admin"),
    path("admin/moradores/<int:id_morador>/", views.MoradoresInfoView.as_view(), name="moradores_info_admin"),
    path("admin/moradores/adicionar/", views.MoradoresAddView.as_view(), name="moradores_add"),
    path("admin/moradores/<int:pk>/alterar/", views.MoradoresUpdView.as_view(), name="moradores_upd"),
    path("admin/moradores/<int:pk>/deletar/", views.MoradoresDelView.as_view(), name="moradores_del"),
    path("admin/reunioes/", views.ReunioesListaView.as_view(), name="reunioes_lista_admin"),
    path("admin/reunioes/adicionar/", views.ReunioesAddView.as_view(), name="reunioes_add"),
    path("admin/reclamacoes/", views.ReclamacoesListaView.as_view(), name="reclamacoes_lista_admin"),
    path("admin/reclamacoes/adicionar/", views.ReclamacoesAddView.as_view(), name="reclamacoes_add"),
    path("admin/avisos/", views.AvisosListaView.as_view(), name="avisos_lista_admin"),
    path("admin/avisos/adicionar/", views.AvisosAddView.as_view(), name="avisos_add"),
]
