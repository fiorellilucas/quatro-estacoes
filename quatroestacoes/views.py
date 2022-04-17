from unicodedata import name
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from django.views.generic.edit import FormView
from django.views.generic import ListView
from django.urls import path

from .forms import MoradorForm
from . import views, models


class IndexView(View):

    def get(self, request):
        return HttpResponse("<h1>Hello, World!</h1>")


class AdminView(View):
    
    def get(self, request):
        return HttpResponse("<h1>Página do admin</h1>")

    #TODO: Criar AdminView para adicionar, alterar, remover moradores, avisos e reuniões
    #TODO: Criar template básica para cada um deles


class LoginView(View):

    def get(self, request, *args, **kwargs):
        return HttpResponse("<h1>Página de login</h1>")


class MoradorView(ListView):
    
    model = models.Morador 
    context = models.Morador.objects.all()
    context_object_name = "moradores"
    template_name = "quatroestacoes/moradores/lista.html"
    

class MoradorAddView(FormView):
    template_name = "quatroestacoes/moradores/adicionar.html"
    form_class = MoradorForm
    success_url = "../../" # quatroestacoes/
    
    #TODO: def form_valid()
    #TODO: Criar usuário
    