from django.urls import path, include
from . import views

urlpatterns = [
    path('cadastrarfuncionario/', views.cadastro, name='cadastro'),
    path('funcionarios/', views.funcionarios, name="funcionarios"),
    path('cadastrarnoticia/', views.cadastrarnoticia, name="cadastrarnoticia"),
    path('noticias/', views.noticias, name="noticias"),
    path('', views.login, name="login")
]
