from django.shortcuts import render
from receita.models import Categoria
from .form import CategoriaForm
from django.views.generic import ListView,CreateView,DeleteView,DetailView, UpdateView,TemplateView
from django.urls import reverse_lazy
from django.contrib.messages import views
from users.permissions import GerentePermission
from receita.models import Receita
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from users.models import User

    
class areaAdmin(ListView):
    template_name = 'categoria/areaAdmin.html'
    paginate_by = 3

    def get(self, request, *args, **kwargs):
        categorias = Categoria.objects.all()
        receitas = Receita.objects.all()
        usuarios = User.objects.all()

        categorias_paginator = Paginator(categorias, self.paginate_by)
        categorias_page = request.GET.get('categorias_page', 1)
        categorias = categorias_paginator.get_page(categorias_page)

        receitas_paginator = Paginator(receitas, self.paginate_by)
        receitas_page = request.GET.get('receitas_page', 1)
        receitas = receitas_paginator.get_page(receitas_page)

        usuarios_paginator = Paginator(usuarios, self.paginate_by)
        usuarios_page = request.GET.get('usuarios_page', 1)
        usuarios = usuarios_paginator.get_page(usuarios_page)

        context = {
            'categorias': categorias,
            'receitas': receitas,
            'usuarios': usuarios,
            'total_receitas': Receita.objects.count(),
            'total_categoria': Categoria.objects.count(),
            'total_usuarios': User.objects.count(),
        }
        return render(request, self.template_name, context)


class cadastroCategoria(CreateView):
    form_class = CategoriaForm
    model = Categoria
    template_name = 'categoria/formCategoria.html'
    success_url = reverse_lazy('areaAdmin')

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

