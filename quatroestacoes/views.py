from django.views.generic import ListView, TemplateView, DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetConfirmView, PasswordResetCompleteView, PasswordResetDoneView, PasswordResetView
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy

from rest_framework import viewsets, permissions

from itertools import chain

from . import models, forms, serializers


class MoradorViewSet(viewsets.ModelViewSet):

    queryset = models.Morador.objects.all()
    serializer_class = serializers.MoradorSerializer
    permission_classes = [permissions.AllowAny]


class ReservaViewSet(viewsets.ModelViewSet):

    queryset = models.Reserva.objects.all()
    serializer_class = serializers.ReservaSerializer
    permission_classes = [permissions.AllowAny]


class ReuniaoViewSet(viewsets.ModelViewSet):

    queryset = models.Reuniao.objects.all()
    serializer_class = serializers.ReuniaoSerializer
    permission_classes = [permissions.AllowAny]


class AvisoViewSet(viewsets.ModelViewSet):

    queryset = models.Aviso.objects.all()
    serializer_class = serializers.AvisoSerializer
    permission_classes = [permissions.AllowAny]


class ReclamacaoViewSet(viewsets.ModelViewSet):

    queryset = models.Reclamacao.objects.all()
    serializer_class = serializers.ReclamacaoSerializer
    permission_classes = [permissions.AllowAny]


class MyLoginView(LoginView):

    template_name = "quatroestacoes/login.html"
    next_page = "quatroestacoes:index"
    redirect_authenticated_user = True
    form_class = forms.MyLoginForm


class MyLogoutView(LogoutView):

    next_page = "quatroestacoes:login"


class MudarSenhaView(PasswordResetView):

    extra_email_context = {
        "site_name": "Condomínio Quatro Estações"
    }
    template_name = "quatroestacoes/mudar-senha/email.html"


class MudarSenhaPronto(PasswordResetDoneView):

    template_name = "quatroestacoes/mudar-senha/pronto.html"


class MudarSenhaConfirmar(PasswordResetConfirmView):

    template_name = "quatroestacoes/mudar-senha/confirmar.html"
    form_class = forms.AlterarSenhaForm


class MudarSenhaCompletar(PasswordResetCompleteView):

    template_name = "quatroestacoes/mudar-senha/completar.html"


class IndexView(LoginRequiredMixin, TemplateView):

    template_name = "quatroestacoes/index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context["avisos"] = models.Aviso.objects.all().order_by(
            "-data_postagem")[:4]
        context["reservas"] = models.Reserva.objects.filter(
            data__gte=timezone.localdate()).order_by("data")[:6]
        return context


class CalendarioView(LoginRequiredMixin, TemplateView):

    template_name = "quatroestacoes/calendario.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        reservas = list(models.Reserva.objects.all().values())
        reunioes = list(models.Reuniao.objects.all().values())

        for reuniao in reunioes:
            reuniao["data"] = timezone.localtime(reuniao["data"]).date()
            reuniao["tipo_evento"] = "reuniao"

        for reserva in reservas:
            morador = models.Morador.objects.get(pk=reserva["morador_id"])
            reserva["morador_nome"] = morador.first_name
            reserva["morador_sobrenome"] = morador.last_name
            reserva["tipo_evento"] = "reserva"

        eventos = list(chain(reunioes, reservas))
        eventos = sorted(eventos, key=lambda t: t["data"])

        context["eventos"] = eventos

        return context


class MoradoresListaView(LoginRequiredMixin, ListView):

    model = models.Morador
    context = models.Morador.objects.all()
    context_object_name = "moradores"
    template_name = "quatroestacoes/moradores/lista.html"


class MoradoresInfoView(LoginRequiredMixin, DetailView):

    model = models.Morador

    def get(self, request, id_morador):
        morador = models.Morador.objects.get(pk=id_morador)
        response = render(
            request, "quatroestacoes/moradores/info.html", {"morador": morador})

        return response


class ReunioesListaView(LoginRequiredMixin, ListView):

    model = models.Reuniao
    template_name = "quatroestacoes/reunioes/lista.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["reunioes"] = models.Reuniao.objects.filter(
            data__gte=timezone.localdate()).order_by("data")
        return context


class ReunioesInfoView(LoginRequiredMixin, DetailView):
    model = models.Reuniao
    template_name = "quatroestacoes/reunioes/info.html"
    context_object_name = "reuniao"


class ReclamacoesListaView(LoginRequiredMixin, ListView):

    model = models.Reclamacao
    template_name = "quatroestacoes/reclamacoes/lista.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["reclamacoes"] = models.Reclamacao.objects.all().order_by(
            "-data_postagem")
        return context


class ReclamacoesInfoView(LoginRequiredMixin, DetailView):

    model = models.Reclamacao
    template_name = "quatroestacoes/reclamacoes/info.html"
    context_object_name = "reclamacao"


class ReclamacoesAddView(LoginRequiredMixin, CreateView):

    model = models.Reclamacao
    template_name = "quatroestacoes/reclamacoes/adicionar.html"
    form_class = forms.ReclamacaoForm
    success_url = reverse_lazy("quatroestacoes:reclamacoes_lista")


class ReclamacoesUpdView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):

    model = models.Reclamacao
    template_name = "quatroestacoes/reclamacoes/alterar.html"
    form_class = forms.ReclamacaoForm
    success_url = reverse_lazy("quatroestacoes:reclamacoes_lista")

    login_url = "quatroestacoes:index"
    redirect_field_name = None

    def test_func(self):
        return self.request.user.is_staff


class ReclamacoesDelView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):

    model = models.Reclamacao
    template_name = "quatroestacoes/reclamacoes/deletar.html"
    success_url = reverse_lazy("quatroestacoes:reclamacoes_lista")
    context_object_name = "reclamacao"

    login_url = "quatroestacoes:index"
    redirect_field_name = None

    def test_func(self):
        return self.request.user.is_staff


class AvisosListaView(LoginRequiredMixin, ListView):

    model = models.Aviso
    template_name = "quatroestacoes/avisos/lista.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["avisos"] = models.Aviso.objects.all().order_by(
            "-data_postagem")
        return context


class AvisosInfoView(LoginRequiredMixin, DetailView):

    model = models.Aviso
    template_name = "quatroestacoes/avisos/info.html"
    context_object_name = "aviso"


class ReservasListaView(LoginRequiredMixin, ListView):

    model = models.Reserva
    template_name = "quatroestacoes/reservas/lista.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["reservas"] = models.Reserva.objects.filter(
            data__gte=timezone.localdate()).order_by("data")
        return context


class ReservasAddView(LoginRequiredMixin, CreateView):

    model = models.Reserva
    template_name = "quatroestacoes/reservas/adicionar.html"
    form_class = forms.ReservaForm
    success_url = reverse_lazy("quatroestacoes:calendario")
