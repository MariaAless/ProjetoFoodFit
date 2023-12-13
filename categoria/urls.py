from django.urls import path
from . import views


urlpatterns = [
  
    path('categoria/areaAdmin/', views.areaAdmin.as_view(), name='areaAdmin'),
    path('cadastroCategoria/',views.cadastroCategoria.as_view(), name='cadastroCategoria'),
    path('categoria/atualizarCategoria/<int:pk>/',views.atualizarCategoria.as_view(), name='atualizarCategoria'),
    path('categoria/deleteCategoria/<int:pk>/',views.deleteCategoria.as_view(), name='deleteCategoria'),
    path('categoria/deleteReceita/<int:pk>/',views.deleteReceita.as_view(), name='deleteReceita'),
    path('categoria/deleteUsuario/<int:pk>/',views.deleteUsuario.as_view(), name='deleteUsuario'),
    path('categoria/receitadetalhe/<int:pk>/',views.receitadetalhe.as_view(), name='receitadetalhe'),
 
   

    
   
    
]