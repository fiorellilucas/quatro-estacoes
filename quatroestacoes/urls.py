from django.urls import path
from . import views

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("login/", views.LoginView.as_view(), name="login"),  #TODO: Redirecionar todas as páginas para login/ se não estiver logado
    path("admin/", views.AdminView.as_view(), name="admin"),
    path("admin/moradores", views.MoradorView.as_view(), name="moradores"),
    path("admin/moradores/adicionar", views.MoradorAddView.as_view(), name="morador_add")
]