from django.http import HttpResponse
from django.views import View
from django.views.generic import ListView, TemplateView, DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User

from . import models, forms

# quatroestacoes/admin
ADMIN_INDEX_URL = "/quatroestacoes/admin" 

# quatroestacoes/
SUCCESS_INDEX_URL = "/quatroestacoes/" 


class IndexView(ListView):

    model = models.Aviso
    context = models.Aviso.objects.all()
    context_object_name = "avisos"
    template_name = "quatroestacoes/index.html"


class LoginView(View):

    def get(self, request):
        return HttpResponse("<h1>Página de login</h1>")


class AdminIndexView(TemplateView): 
    
    template_name = 'quatroestacoes/admin/index.html'


class MoradoresListaView(ListView):    
    
    model = models.Morador 
    context = models.Morador.objects.all()
    context_object_name = "moradores"
    template_name = "quatroestacoes/moradores/lista.html"


class MoradoresInfoView(DetailView):
    
    model = models.Morador

    def get(self, request, id_morador):
        morador = models.Morador.objects.get(pk=id_morador)
        response = render(request, "quatroestacoes/moradores/info.html", {"morador": morador})

        return response


class MoradoresAddView(CreateView):
    
    model = models.Morador
    template_name = "quatroestacoes/moradores/adicionar.html"
    form_class = forms.MoradorForm
    success_url = ADMIN_INDEX_URL

    def form_valid(self, form):
        form.criar_usuario()

        return super().form_valid(form)


class MoradoresUpdView(UpdateView):

    model = models.Morador
    fields = "__all__"
    template_name = "quatroestacoes/moradores/alterar.html"
    success_url = ADMIN_INDEX_URL


class MoradoresDelView(DeleteView):

    model = models.Morador
    template_name = "quatroestacoes/moradores/deletar.html"
    success_url = ADMIN_INDEX_URL

    def post(self, request, *args, **kwargs):
        morador = models.Morador.objects.get(pk=kwargs.get("pk"))
        username_morador = f"{morador.nome.lower().split()[0]}{morador.sobrenome.lower().split()[0]}"
        usuario = get_object_or_404(User, username=username_morador)
        usuario.delete()

        return super().post(self, request, *args, **kwargs)


class ReunioesListaView(ListView):
    
    model = models.Reuniao
    context = models.Reuniao.objects.all()
    context_object_name = "reunioes"
    template_name = "quatroestacoes/reunioes/lista.html"


class ReunioesAddView(CreateView):
    
    model = models.Reuniao
    template_name = "quatroestacoes/reunioes/adicionar.html"
    form_class = forms.ReuniaoForm
    success_url = SUCCESS_INDEX_URL


class ReclamacoesListaView(ListView):
    
    model = models.Reclamacao
    context = models.Reclamacao.objects.all()
    context_object_name = "reclamacoes"
    template_name = "quatroestacoes/reclamacoes/lista.html"


class ReclamacoesAddView(CreateView):
    
    model = models.Reclamacao
    template_name = "quatroestacoes/reclamacoes/adicionar.html"
    form_class = forms.ReclamacaoForm
    success_url = SUCCESS_INDEX_URL


class AvisosListaView(ListView):
    
    model = models.Aviso
    context = models.Aviso.objects.all()
    context_object_name = "avisos"
    template_name = "quatroestacoes/avisos/lista.html"


class AvisosAddView(CreateView):
    
    model = models.Aviso
    template_name = "quatroestacoes/avisos/adicionar.html"
    form_class = forms.AvisoForm
    success_url = SUCCESS_INDEX_URL

