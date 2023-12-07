from django import forms
from .models import Receita, Categoria
from datetime import date



class ReceitaForm(forms.ModelForm):
    class Meta:
        model = Receita
        fields = "__all__"

    widgets = {
            'nome' : forms.TextInput(attrs={'class': 'form-control'}),
            'ingredientes' : forms.TextInput(attrs={'class': 'form-control' }),
            'modo_preparo' : forms.TextInput(attrs={'class': 'form-control' }),
            'data_cadastro' : forms.TextInput(attrs={'class': 'form-control' }),
            'categoria' : forms.TextInput(attrs={'class': 'form-control' }),
            'img' : forms.TextInput(attrs={'class': 'form-control' }),
      
        }
       
class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = "__all__"

    

        widgets = {
            'nome' : forms.TextInput(attrs={'class': 'form-control'}),
           
      
        }


        
    
