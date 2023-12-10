from django.shortcuts import render
from receita.models import Categoria
from .form import CategoriaForm
from django.views.generic import ListView,CreateView,DeleteView,DetailView, UpdateView,TemplateView
from django.urls import reverse_lazy
from django.contrib.messages import views
from users.permissions import GerentePermission
from receita.models import Receita



class cadastroCategoria(CreateView):
    form_class = CategoriaForm
    model = Categoria
    template_name = 'categoria/formCategoria.html'
    success_url = reverse_lazy('areaAdmin')
    


class areaAdmin(ListView):
    template_name = 'categoria/areaAdmin.html'
    context_object_name = 'listas'

    def get_queryset(self):
        # Combine as listas de categorias e receitas
        categorias = Categoria.objects.all()
        receitas = Receita.objects.all()
        return {'categorias': categorias, 'receitas': receitas}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(self.get_queryset())
        context['total_receitas'] = Receita.objects.count()
        context['total_categoria'] = Categoria.objects.count()
        return context


class deleteCategoria(views.SuccessMessageMixin,DeleteView):
    model = Categoria
    template_name = 'categoria/confirm.html'
    context_object_name= "categoria"
    success_url = reverse_lazy("categoria:areaAdmin")
    success_message = "categoria deletada com sucesso!"



class atualizarCategoria(views.SuccessMessageMixin,UpdateView):
  model = Categoria
  form_class = CategoriaForm
  success_url = reverse_lazy("listas")
  template_name = "categoria/formCategoria.html"
  success_message = "Categoria atualizado com sucesso!"





class delete(DeleteView):
    model = Receita
    template_name = 'receita/confirm.html'
    success_url = reverse_lazy("areaAdmin")
    context_object_name= "receitas"
  #  success_message = "Reserva deletada com sucesso!"

