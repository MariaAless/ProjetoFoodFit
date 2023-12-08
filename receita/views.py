from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.shortcuts import render,get_object_or_404, redirect
from .models import Receita
from .form import ReceitaForm,CategoriaForm
from django.views.generic import ListView,CreateView,DeleteView,DetailView, UpdateView,TemplateView
from django.urls import reverse_lazy
from django.db.models import Q

class index(TemplateView):
    template_name = 'receita/index.html'

class home(ListView):
    template_name = 'receita/home.html'
    model = Receita
    context_object_name = 'receitas'
    queryset = Receita.objects.all()

    def get_queryset(self):
        return self.queryset.filter(usuario=self.request.user)


class mural(ListView):
    template_name = 'receita/mural.html'
    model = Receita
    context_object_name = 'receitas'
    queryset = Receita.objects.all()

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Receita.objects.filter(Q(nome__icontains=query) | Q(categoria__nome__icontains=query))
        else:
            return Receita.objects.all()



class cadastroReceita(CreateView):
    form_class = ReceitaForm
    model = Receita
    template_name = 'receita/formReserva.html'
    success_url = reverse_lazy('home')
  #  success_message = "Reserva criada com sucesso!"

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)

class receitadetalhe(DetailView):
    model = Receita
    template_name = "receita/detalhe.html"


class receitaeditar(UpdateView):
  model = Receita
  form_class =  ReceitaForm
  success_url = reverse_lazy("mural")
  template_name = 'receita/formReserva.html'
 # success_message = "Reserva atualizada com sucesso!"
class delete(DeleteView):
    model = Receita
    template_name = 'receita/confirm.html'
    success_url = reverse_lazy("mural")
    context_object_name= "receitas"
  #  success_message = "Reserva deletada com sucesso!"

