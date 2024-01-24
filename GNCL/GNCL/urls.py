from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.dashboard, name="dashboard"),
    path('noticias/', include('autenticacao.urls')),
    path('funcionarios/', include('funcionarios.urls')),
    path('accounts/', include('django.contrib.auth.urls'))
]
