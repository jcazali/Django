from django.contrib import admin
# importando o model criado
from .models import Categoria, Transacao

admin.site.register(Categoria)
admin.site.register(Transacao)
