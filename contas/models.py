'''Aqui criam-se os models, classes que farão interação com o banco de dados. 
todo model deve herdar de models.Model, passados como parâmetros entre parentes. 
Categoria é o nome da tabela no banco'''

from django.db import models

class Categoria(models.Model):
    # fields são colunas da tabela. A variável name receberá um texto com no máximo 100 caracteres
    nome = models.CharField(max_length=100)
    # variável que pegará a data e hora atual
    dt_criacao = models.DateTimeField(auto_now_add=True)
    
    # corrigir object(), na tela admin
    def __str__(self):
        return self.nome
    
class Transacao(models.Model):
    # sem parâmetros, é possível adicionar a data manualmente
    data = models.DateField()
    descricao = models.CharField(max_length=200)
    valor = models.DecimalField(max_digits=7, decimal_places=2)
    # relacionamento entre as tabelas
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    # campo com preenchimento não obrigatório
    observacoes = models.TextField(null=True, blank=True)
    
    # maneira de definir como aparecerá o plural do nome da classe na tela admin
    class Meta:
        verbose_name_plural = 'Transacoes'
        
    # maneira de definir como aparecer a descrição na tela admin
    def __str__(self):
        return self.descricao