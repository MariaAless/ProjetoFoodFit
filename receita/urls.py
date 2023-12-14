from django.urls import path
from . import views


urlpatterns = [
    path('',views.index.as_view(), name='index'), 
    path('home/',views.home.as_view(), name="home"),
    path('cadastroReceita/',views.cadastroReceita.as_view(), name='cadastroReceita'),
    path('mural/',views.mural.as_view(), name='mural'),
    path('receitadetalheUsuario/<int:pk>/',views.receitadetalheUsuario.as_view(), name='receitadetalheUsuario'),
    path('receitadetalheMural/<int:pk>/',views.receitadetalheMural.as_view(), name='receitadetalheMural'),
    path('receitaeditar/<int:pk>/',views.receitaeditar.as_view(), name='receitaeditar'),
  #  path('delete/<int:pk>/',views.delete.as_view(), name='delete'),
    path('delete_receita/<int:pk>/', views.DeleteReceita.as_view(), name='delete_receita'),
    
   
    
]