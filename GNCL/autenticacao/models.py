from django.db.models.fields import CharField
from django.db import models
from django.contrib.auth import get_user_model

class Funcionario(models.Model):
    name = CharField(max_length=100)
    login = CharField(max_length=100)
    password = CharField(max_length=100)

class Noticia(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    texto = models.TextField()
    legenda = models.CharField(max_length=100)
    categoria = models.CharField(max_length=100)
    data_e_hora = models.DateTimeField()
    id_funcionario = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True)
