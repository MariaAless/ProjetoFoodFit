from django.shortcuts import render,redirect
from receita.models import Categoria, Comentario
from .form import CategoriaForm
from receita.form import ComentarioForm
from django.views.generic import ListView,CreateView,DeleteView,DetailView, UpdateView,TemplateView
from django.urls import reverse_lazy
from django.contrib.messages import views
from users.permissions import GerentePermission
from receita.models import Receita
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from users.models import User
from django.contrib import messages
from django.urls import reverse_lazy


    
class areaAdmin(GerentePermission,ListView):
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


class cadastroCategoria(GerentePermission,views.SuccessMessageMixin,CreateView):
    form_class = CategoriaForm
    model = Categoria
    template_name = 'categoria/formCategoria.html'
    success_url = reverse_lazy('areaAdmin')
    success_message = "categoria cadastrada com sucesso!"

class deleteCategoria(views.SuccessMessageMixin,DeleteView):
    model = Categoria
    template_name = 'categoria/confirm.html'
    context_object_name= "categorias"
    success_url = reverse_lazy("areaAdmin")
    success_message = "categoria deletada com sucesso!"

class deleteUsuario(views.SuccessMessageMixin,DeleteView):
    model = User
    template_name = 'categoria/confirmDeleteUsuario.html'
    context_object_name= "usuarios"
    success_url = reverse_lazy("areaAdmin")
    success_message = "usuario deletado com sucesso!"

class deleteReceita(views.SuccessMessageMixin,DeleteView):
    model = Receita
    template_name = 'categoria/confirmDeleteReceita.html'
    success_url = reverse_lazy("areaAdmin")
    context_object_name= "receitas"
    success_message = "Reserva deletada com sucesso!"


class atualizarCategoria(views.SuccessMessageMixin,UpdateView):
  model = Categoria
  form_class = CategoriaForm
  success_url = reverse_lazy("areaAdmin")
  template_name = "categoria/formCategoria.html"
  success_message = "Categoria atualizado com sucesso!"



class receitadetalhe(DetailView):
    model = Receita
    template_name = "receita/detalheMural.html"
# ---------------Para o COMENTARIO-----------------
    context_object_name = "receita"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comentarios'] = Comentario.objects.filter(receita=self.object)
        context['form_comentario'] = ComentarioForm()
        return context

    def post(self, request, *args, **kwargs):
        receita = self.get_object()
        form_comentario = ComentarioForm(request.POST)

        if form_comentario.is_valid():
            comentario = form_comentario.save(commit=False)
            comentario.usuario = self.request.user
            comentario.receita = receita
            comentario.save()
            messages.success(request, 'Comentário adicionado com sucesso.')
            return redirect('receitadetalheMural', pk=receita.pk)
        else:
            messages.error(request, 'Erro ao adicionar o comentário.')

        return self.get(request, *args, **kwargs)