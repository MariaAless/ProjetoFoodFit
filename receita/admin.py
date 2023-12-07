from django.contrib import admin
from receita.models import Receita, Categoria
# Register your models here.
@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nome',)
@admin.register(Receita)
class ReceitaAdmin(admin.ModelAdmin):
    list_display = ('img','nome','ingredientes', 'modo_preparo', 'data_cadastro')
