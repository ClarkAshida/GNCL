from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('noticias/', include('autenticacao.urls')),
    path('funcionarios/', include('funcionarios.urls')),
    path('accounts/', include('django.contrib.auth.urls'))
]
