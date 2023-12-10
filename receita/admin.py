from django.contrib import admin
from receita.models import Receita, Categoria,Comentario
# Register your models here.
@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nome',)


class ReceitaAdmin(admin.ModelAdmin):
    list_display = ('nome','ingredientes', 'modo_preparo', 'data_cadastro')

admin.site.register(Receita, ReceitaAdmin)


@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'receita', 'data_criacao')
    search_fields = ('usuario_username', 'receita_nome', 'data_criacao')
    list_filter = ('receita', 'data_criacao')