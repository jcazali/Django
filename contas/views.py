# from django.http import HttpResponse
from django.shortcuts import redirect, render
import datetime
# importando a classe Transacao de models.py
from .models import Transacao
# importando a classe TransacaoForm de form.py
from .form import TrasacaoForm

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

# função que retorna uma lista das transações
def listagem(request):
    # criando um dicionário
    data = {}
    # criando uma variável no dicionário, e passando todas as transações do banco
    data['transacoes'] = Transacao.objects.all()       
    return render(request, 'contas/listagem.html', data)

# função responsável por criar uma nova transação
def nova_transacao(request):
    data = {} 
    form = TrasacaoForm(request.POST or None)

    # se o formulário for válido, ele é salvo no banco e a url listagem é exibida
    if form.is_valid():
        form.save()
        return redirect('listagem')

    data['form'] = form
    return render(request, 'contas/form.html', data)

    # outra maneira de fazer a mesma coisa
    # form = TransacaoForm()
    # return render(request, 'contas/form.html', {'form': form})