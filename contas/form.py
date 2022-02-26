# criando um formulário para preenchimento

# importando classe para manipulação de formulários 
from django.forms import ModelForm
# importando a classe Transação de models.py
from .models import Transacao

# criando uma classe que herda de ModelForm
class TrasacaoForm(ModelForm):
    # criando uma classe com os campos que irão aparecer no formulário
    class Meta:
        model = Transacao()
        fields = ('data', 'descricao', 'valor', 'observacoes', 'categoria')