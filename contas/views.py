from django.shortcuts import render
#from django.http import HttpResponse
import datetime
# importando o model Transacao
from .models import Transacao 

'''def home(request):
    now = datetime.datetime.now()
    html = "<html><body>Agora é %s.</body></html>" % now
    return HttpResponse(html) '''

# função que retorna o arquivo home.html
def home(request):
    # criando um dicionário, com uma variável que será usada em home.html
    data = {}    
    data['now'] = datetime.datetime.now()
    
    # passando o dicionário criado como parâmetro
    return render(request, 'contas/home.html', data)

def listagem(request):
    # criando um dicionário
    data = {}
    # criando uma variável no dicionário, e passando todas as transações do banco
    data['transacoes'] = Transacao.objects.all()
       
    return render(request, 'contas/listagem.html', data)
