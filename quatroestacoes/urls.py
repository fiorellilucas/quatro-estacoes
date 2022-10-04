from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'moradores', views.MoradorViewSet)
router.register(r'reservas', views.ReservaViewSet)
router.register(r'reunioes', views.ReuniaoViewSet)
router.register(r'avisos', views.AvisoViewSet)
router.register(r'reclamacoes', views.ReclamacaoViewSet)

app_name = "quatroestacoes"
urlpatterns = [
    path("", include(router.urls)),
]
