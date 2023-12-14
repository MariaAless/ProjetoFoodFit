from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import  redirect
from .models import Receita,Comentario
from .form import ReceitaForm,ComentarioForm
from django.views.generic import ListView,CreateView,DeleteView,DetailView, UpdateView,TemplateView
from django.urls import reverse_lazy
from django.db.models import Q
from django.contrib import messages
from django.contrib.messages import views

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



class cadastroReceita(views.SuccessMessageMixin,CreateView):
    form_class = ReceitaForm
    model = Receita
    template_name = 'receita/formReceita.html'
    success_url = reverse_lazy('home')
    success_message = "Receita criada com sucesso!"
    

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)

class receitadetalheUsuario(DetailView):
    model = Receita
    template_name = "receita/detalheUsuario.html"
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
            return redirect('receitadetalheUsuario', pk=receita.pk)
        else:
            messages.error(request, 'Erro ao adicionar o comentário.')

        return self.get(request, *args, **kwargs)

class receitadetalheMural(DetailView):
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

class receitaeditar(views.SuccessMessageMixin,UpdateView):
  model = Receita
  form_class =  ReceitaForm
  success_url = reverse_lazy("home")
  template_name = 'receita/formReceita.html'
  success_message = "Reserva atualizada com sucesso!"

class DeleteReceita(views.SuccessMessageMixin,DeleteView):
    model = Receita
    template_name = 'detalheUsuario.html'  # Substitua pelo nome do seu template
    success_url = reverse_lazy('home')  # Redireciona para a página desejada após a exclusão
    success_message = "Receita deletada com sucesso!"
   
    def get_object(self, queryset=None):
        return Receita.objects.get(pk=self.kwargs['pk'])

    def delete(self, request, *args, **kwargs):
        receita = self.get_object()
        # Adicione sua lógica adicional aqui, se necessário
        receita.delete()
        return redirect('home')

