from django.urls import path
from . import views


urlpatterns = [
    path('',views.index.as_view(), name='index'), 
    path('home/',views.home.as_view(), name="home"),
    path('cadastroReceita/',views.cadastroReceita.as_view(), name='cadastroReceita'),
    path('mural/',views.mural.as_view(), name='mural'),
    path('receitadetalhe/<int:pk>/',views.receitadetalhe.as_view(), name='receitadetalhe'),
    path('receitaeditar/<int:pk>/',views.receitaeditar.as_view(), name='receitaeditar'),
    path('delete/<int:pk>/',views.delete.as_view(), name='delete'),
    
   
    
]