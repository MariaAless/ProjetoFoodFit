from django import forms
from .models import Receita, Comentario
from datetime import date


class ReceitaForm(forms.ModelForm):
    class Meta:
        model = Receita
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(ReceitaForm, self).__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})



class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['texto']
        widgets = {
            'texto': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Adicione um comentário...'}),
        }
        labels = {
            'texto': False,
        }

