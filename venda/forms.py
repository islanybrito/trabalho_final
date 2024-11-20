from django import forms
from .models import Cliente
from .models import Produto
from .models import Estoque

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'cpf']
        

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['descricao', 'valor', 'cliente']

class EstoqueForm(forms.ModelForm):
    class Meta:
        model = Estoque
        fields = ['produto', 'quantidade']