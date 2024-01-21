from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.dashboard, name="dashboard"),
    path('cadastrarfuncionario/', views.cadastrarfuncionario, name="cadastrarfuncionario"),
    path('funcionarios/', views.funcionarios, name="funcionarios"),
    path('cadastrarnoticia/', views.cadastrarnoticia, name="cadastrarnoticia"),
    path('noticias/', views.noticias, name="noticias"),
    path('login/', views.login, name="login"),
    path('funcionarios/<int:id>/', views.display_funcionarios, name="funcionarios_id"),
    path('noticias/<int:id>/', views.display_noticias, name="noticias_id"),
    path('editarnoticia/<int:id>', views.editarNoticia, name="editarnoticia"),
    path('deletarnoticia/<int:id>', views.deletarNoticia, name="deletarnoticia"),
    path('editarfuncionario/<int:id>', views.editarFuncionario, name="editarfuncionario"),
    path('deletarfuncionario/<int:id>', views.deletarFuncionario, name="deletarfuncionario")
]
