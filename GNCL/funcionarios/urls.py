from django.urls import path
from . import views

urlpatterns = [
    path('cadastrarfuncionario/', views.SignUp.as_view(), name="cadastrarfuncionario"),
    path('funcionarios/', views.funcionarios, name="funcionarios"),
    path('funcionarios/<int:id>/', views.display_funcionarios, name="funcionarios_id"),
    path('editarfuncionario/<int:id>', views.editarFuncionario, name="editarfuncionario"),
    path('deletarfuncionario/<int:id>', views.deletarFuncionario, name="deletarfuncionario"),
]
