from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', include('autenticacao.urls')),
    path('accounts/', include('django.contrib.auth.urls'))
]
