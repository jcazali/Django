# Arquivo de urls do projeto

from django.contrib import admin
from django.urls import path
# importando a função home do arquivo views.py do diretório contas
from contas.views import home, listagem

urlpatterns = [
    path('admin/', admin.site.urls),
    # '' indica que é será a primeira página a ser exibida
    path('', listagem),
    path('home/', home)
]