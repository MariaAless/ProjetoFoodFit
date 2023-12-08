
from django.db import models
from datetime import date
from django.utils import timezone
from users.models import User


# Create your models here.

class Categoria(models.Model):
    nome= models.CharField(max_length=50)
  

    def __str__(self):
        return self.nome

class Receita(models.Model):
    img=models.ImageField(upload_to="capa_receita", null =True, blank=True)
    nome=models.CharField(max_length=100)
    ingredientes = models.TextField()
    modo_preparo = models.TextField()
    data_cadastro=models.DateField(default=date.today)
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, default=None)

  
    def __str__(self):
        return self.nome


    class Meta:
        verbose_name='Receita'


