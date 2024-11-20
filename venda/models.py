
from django.db import models

#class Produto(models.Model):
    #nome = models.CharField(max_length=200)
   # valor = models.DecimalField(max_digits=10, decimal_places=2)
    #estoque = models.ForeignKey(Estoque, on_delete=models.CASCADE, related_name='produtos')
    #estoque = models.IntegerField()
class Produto(models.Model):
    nome = models.CharField(max_length=200)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    

    def __str__(self):
        return self.nome

class Cliente(models.Model):
    nome = models.CharField(max_length=200)
    cpf = models.CharField(max_length=15, unique=True)
    #email = models.EmailField(unique=True)
    #telefone = models.CharField(max_length=15)

    def __str__(self):
        return self.nome

class Vendedor(models.Model):
    nome = models.CharField(max_length=200)
    cpf = models.CharField(max_length=11, unique=True)
    email = models.EmailField()

    def __str__(self):
        return self.nome

class Venda(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    vendedor = models.ForeignKey(Vendedor, on_delete=models.CASCADE)
    data_venda = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Venda {self.id} - {self.cliente.nome}"

class ItemVenda(models.Model):
    venda = models.ForeignKey(Venda, related_name='itens', on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.IntegerField()
    valor_unitario = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.quantidade} x {self.produto.nome}"

class Pagamento(models.Model):
    venda = models.ForeignKey(Venda, on_delete=models.CASCADE)
    valor_pago = models.DecimalField(max_digits=10, decimal_places=2)
    data_pagamento = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Pagamento {self.id} - Venda {self.venda.id}"



class Estoque(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE, related_name='estoque_itens')
    quantidade = models.IntegerField()


    def __str__(self):
        return f"Estoque de {self.produto.nome}: {self.quantidade} unidades"
