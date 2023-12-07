from django.shortcuts import render
from django.shortcuts import render,get_object_or_404, redirect
from .models import Receita
from .form import ReceitaForm,CategoriaForm
from django.views.generic import ListView,CreateView,DeleteView,DetailView, UpdateView,TemplateView
from django.urls import reverse_lazy

def index(request):
    return render(request, 'receita/index.html')

def home(request):
    return render(request, 'receita/home.html')


class mural(ListView):
    template_name = 'receita/mural.html'
    model = Receita
    context_object_name = 'receitas'
class cadastroReceita(CreateView):

    form_class = ReceitaForm
    template_name = 'receita/formReserva.html'
    success_url = reverse_lazy('home')
  #  success_message = "Reserva criada com sucesso!"

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

