from django.urls import path
from . import views

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("admin/", views.AdminView.as_view(), name="admin"),
    path("login/", views.LoginView.as_view(), name="login"),  #TODO: Redirecionar todas as páginas para login/ se não estiver logado
    
]