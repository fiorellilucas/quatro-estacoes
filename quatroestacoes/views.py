from django.views.generic import ListView, TemplateView, DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetConfirmView, PasswordResetCompleteView, PasswordResetDoneView, PasswordResetView

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from . import models, forms

SUCCESS_INDEX_URL = "/"


class MyLoginView(LoginView):

    template_name = "quatroestacoes/login.html"
    next_page = "quatroestacoes:index"
    redirect_authenticated_user = True


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
    

class IndexView(LoginRequiredMixin, ListView):

    model = models.Aviso
    context = models.Aviso.objects.all()
    context_object_name = "avisos"
    template_name = "quatroestacoes/index.html"


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


class MoradoresAddView(LoginRequiredMixin, UserPassesTestMixin, CreateView):

    model = models.Morador
    template_name = "quatroestacoes/moradores/adicionar.html"
    form_class = forms.MoradorCreationForm
    success_url = SUCCESS_INDEX_URL

    redirect_field_name = None

    def test_func(self):
        return self.request.user.is_staff


class MoradoresUpdView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):

    model = models.Morador
    template_name = "quatroestacoes/moradores/alterar.html"
    form_class = forms.MoradorChangeForm
    success_url = SUCCESS_INDEX_URL

    login_url = "quatroestacoes:index"
    redirect_field_name = None

    def test_func(self):
        return self.request.user.is_staff


class MoradoresDelView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):

    model = models.Morador
    template_name = "quatroestacoes/moradores/deletar.html"
    success_url = SUCCESS_INDEX_URL
    context_object_name = "morador"

    login_url = "quatroestacoes:index"
    redirect_field_name = None

    def test_func(self):
        return self.request.user.is_staff


class CalendarioView(LoginRequiredMixin, TemplateView):

    template_name = "quatroestacoes/calendario.html"


class ReunioesListaView(LoginRequiredMixin, ListView):

    model = models.Reuniao
    context = models.Reuniao.objects.all()
    context_object_name = "reunioes"
    template_name = "quatroestacoes/reunioes/lista.html"


class ReunioesAddView(LoginRequiredMixin, CreateView):

    model = models.Reuniao
    template_name = "quatroestacoes/reunioes/adicionar.html"
    form_class = forms.ReuniaoForm
    success_url = SUCCESS_INDEX_URL


class ReclamacoesListaView(LoginRequiredMixin, ListView):

    model = models.Reclamacao
    context = models.Reclamacao.objects.all()
    context_object_name = "reclamacoes"
    template_name = "quatroestacoes/reclamacoes/lista.html"
    
    
class ReclamacoesInfoView(LoginRequiredMixin, DetailView):
    
    model = models.Reclamacao
    template_name = "quatroestacoes/reclamacoes/info.html"
    context_object_name = "reclamacao"


class ReclamacoesAddView(LoginRequiredMixin, CreateView):

    model = models.Reclamacao
    template_name = "quatroestacoes/reclamacoes/adicionar.html"
    form_class = forms.ReclamacaoForm
    success_url = SUCCESS_INDEX_URL


class AvisosListaView(LoginRequiredMixin, ListView):

    model = models.Aviso
    context = models.Aviso.objects.all()
    context_object_name = "avisos"
    template_name = "quatroestacoes/avisos/lista.html"
    
    
class AvisosInfoView(LoginRequiredMixin, DetailView):
    
    model = models.Aviso
    template_name = "quatroestacoes/avisos/info.html"
    context_object_name = "aviso"


class AvisosAddView(LoginRequiredMixin, CreateView):

    model = models.Aviso
    template_name = "quatroestacoes/avisos/adicionar.html"
    form_class = forms.AvisoForm
    success_url = SUCCESS_INDEX_URL


class ReservasListaView(LoginRequiredMixin, ListView):

    model = models.Reserva
    context = models.Reserva.objects.all()
    context_object_name = "reservas"
    template_name = "quatroestacoes/reservas/lista.html"


class ReservasAddView(LoginRequiredMixin, CreateView):

    model = models.Reserva
    template_name = "quatroestacoes/reservas/adicionar.html"
    form_class = forms.ReservaForm
    success_url = SUCCESS_INDEX_URL
