from django.shortcuts import render
from django.http import HttpResponse
from django.views import View


class IndexView(View):

    def get(self, request, *args, **kwargs):
        return HttpResponse("<h1>Hello, World!</h1>")


class AdminView(View):
    
    def get(self, request, *args, **kwargs):
        return HttpResponse("<h1>Página do admin</h1>")

    #TODO: Criar AdminView para adicionar, alterar, remover moradores, avisos e reuniões
    #TODO: Criar template básica para cada um deles


class LoginView(View):

    def get(self, request, *args, **kwargs):
        return HttpResponse("<h1>Página de login</h1>")
    