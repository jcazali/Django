# Arquivo de urls do projeto

from django.contrib import admin
from django.urls import path
# importando funções de views.py do diretório contas
from contas.views import home, listagem, nova_transacao

urlpatterns = [
    path('admin/', admin.site.urls),
    # '' indica que é será a primeira página a ser exibida
    path('', listagem, name= 'listagem'),
    path('nova/', nova_transacao, name= 'nova'),
    path('home/', home)
]