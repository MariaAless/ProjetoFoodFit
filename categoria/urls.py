from django.urls import path
from . import views


urlpatterns = [
  
    path('categoria/areaAdmin/', views.areaAdmin.as_view(), name='areaAdmin'),
    path('cadastroCategoria/',views.cadastroCategoria.as_view(), name='cadastroCategoria'),
    path('categoria/atualizarCategoria/<int:pk>/',views.atualizarCategoria.as_view(), name='atualizarCategoria'),
    path('categoria/deleteCategoria/<int:pk>/',views.deleteCategoria.as_view(), name='deleteCategoria'),
  
   

    
   
    
]