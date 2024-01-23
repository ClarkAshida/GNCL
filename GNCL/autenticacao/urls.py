from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.dashboard, name="dashboard"),
    path('cadastrarnoticia/', views.cadastrarnoticia, name="cadastrarnoticia"),
    path('noticias/', views.noticias, name="noticias"),
    path('noticias/<int:id>/', views.display_noticias, name="noticias_id"),
    path('editarnoticia/<int:id>', views.editarNoticia, name="editarnoticia"),
    path('deletarnoticia/<int:id>', views.deletarNoticia, name="deletarnoticia"),
]
