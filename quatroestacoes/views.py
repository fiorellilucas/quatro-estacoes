from multiprocessing import context
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from django.views.generic.edit import FormView
from django.views.generic import ListView, TemplateView

from . import models, forms

# quatroestacoes/admin
ADMIN_INDEX_URL = "/quatroestacoes/admin" 


class IndexView(View):

    def get(self, request):
        return HttpResponse("<h1>Hello, World!</h1>")


class AdminView(TemplateView): 
    template_name = 'quatroestacoes/admin/index.html'


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
    form_class = forms.MoradorForm
    success_url = ADMIN_INDEX_URL

    def form_valid(self, form):
        form.adicionar_morador()
        form.criar_usuario()

        return super().form_valid(form)


class ReuniaoView(ListView):
    model = models.Reuniao
    context = models.Reuniao.objects.all()
    context_object_name = "reunioes"
    template_name = "quatroestacoes/reunioes/lista.html"


class ReuniaoAddView(FormView):
    template_name = "quatroestacoes/reunioes/adicionar.html"
    form_class = forms.ReuniaoForm
    success_url = ADMIN_INDEX_URL
    
    def form_valid(self, form):
        form.criar_reuniao()

        return super().form_valid(form)