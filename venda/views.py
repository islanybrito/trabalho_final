from django.shortcuts import render, redirect, get_object_or_404
from .models import Cliente
from .models import Produto
from .models import Estoque
from .forms import ClienteForm
from .forms import ProdutoForm
from .forms import EstoqueForm
from django.contrib.auth.decorators import login_required
from weasyprint import HTML
from django.http import HttpResponse
from django.template.loader import render_to_string


@login_required
def listar_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'clientes/listar_clientes.html' , {'clientes': clientes})

@login_required
def criar_cliente(request):
    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_clientes')
    else:
        form = ClienteForm()
    return render(request, 'clientes/criar_clientes.html', {'form':form})

@login_required
def atualizar_cliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)
    if request.method == "POST":
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('listar_clientes')
    else:
        form = ClienteForm(instance=cliente)
    return render(request, 'clientes/atualizar_cliente.html', {'form': form})

@login_required
def deletar_cliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)
    if request.method == "POST":
        cliente.delete()
        return redirect('listar_clientes')
    return render(request, 'clientes/deletar_cliente.html', {'cliente': cliente})


@login_required
def listar_produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'produtos/listar_produtos.html', {'produtos': produtos})

@login_required
def criar_produto(request):
    if request.method == "POST":
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_produtos')
    else:
        form = ProdutoForm()
    return render(request, 'produtos/criar_produto.html', {'form': form})

@login_required
def atualizar_produto(request, id):
    produto = get_object_or_404(Produto, id=id)
    if request.method == "POST":
        form = ProdutoForm(request.POST, instance=produto)
        if form.is_valid():
            form.save()
            return redirect('listar_produtos')
    else:
        form = ProdutoForm(instance=produto)
    return render(request, 'produtos/atualizar_produto.html', {'form': form})

@login_required
def deletar_produto(request, id):
    produto = get_object_or_404(Produto, id=id)
    if request.method == "POST":
        produto.delete()
        return redirect('listar_produtos')  # Redireciona para a lista de 
    return render(request, 'produtos/deletar_produto.html', {'produto':produto})

@login_required
def exportar_clientes_pdf(request):
    # Buscando todos os usuários
    clientes = Cliente.objects.all()

    # Renderizando o template HTML com os dados dos usuários
    html_string = render_to_string('clientes/clientes_pdf.html', {'clientes': clientes})

    # Criando a resposta HTTP para o PDF
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="clientes.pdf"'

    # Convertendo o HTML para PDF usando WeasyPrint
    HTML(string=html_string).write_pdf(response)

    return response

@login_required
def exportar_produtos_pdf(request):
    # Buscando todos os usuários
    produtos = Produto.objects.all()

    # Renderizando o template HTML com os dados dos usuários
    html_string = render_to_string('produtos/produtos_pdf.html', {'produtos': produtos})

    # Criando a resposta HTTP para o PDF
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="clientes.pdf"'

    # Convertendo o HTML para PDF usando WeasyPrint
    HTML(string=html_string).write_pdf(response)

    return response

@login_required
def listar_estoques(request):
    estoques = Estoque.objects.all()
    return render(request, 'estoques/listar_estoques.html' , {'estoques': estoques})

@login_required
def criar_estoque(request):
    if request.method == "POST":
        form = EstoqueForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_estoques')
    else:
        form = EstoqueForm()
    return render(request, 'estoques/criar_estoque.html', {'form': form})

@login_required
def atualizar_estoque(request, id):
    estoques = get_object_or_404(Estoque, id=id)
    if request.method == "POST":
        form = EstoqueForm(request.POST, instance=estoques)
        if form.is_valid():
            form.save()
            return redirect('listar_estoques')
    else:
        form = EstoqueForm(instance=estoques)
    return render(request, 'estoques/atualizar_estoques.html', {'form': form})

@login_required
def deletar_estoque(request, id):
    estoque = get_object_or_404(Produto, id=id)
    if request.method == "POST":
        estoque.delete()
        return redirect('listar_estoques')  # Redireciona para a lista de 
    return render(request, 'estoques/deletar_estoque.html', {'estoque':estoque})

@login_required
def exportar_estoque_pdf(request):
    # Buscando todos os usuários
    estoques = Cliente.objects.all()

    # Renderizando o template HTML com os dados dos usuários
    html_string = render_to_string('estoques/estoque_pdf.html', {'estoques': estoques})

    # Criando a resposta HTTP para o PDF
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="estoques.pdf"'

    # Convertendo o HTML para PDF usando WeasyPrint
    HTML(string=html_string).write_pdf(response)

    return response

