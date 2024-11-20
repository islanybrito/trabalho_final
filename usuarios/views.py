from django.shortcuts import render, redirect, get_object_or_404
from .forms import UsuarioForm
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from weasyprint import HTML
from django.http import HttpResponse
from django.template.loader import render_to_string
# Create your views here.

Usuario = get_user_model()

@login_required
def listar_usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'usuarios/listar_usuarios.html', {'usuarios': usuarios})
@login_required
def criar_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_usuarios')
    else:
        form = UsuarioForm()
    return render(request, 'usuarios/criar_usuario.html', {'form': form})

@login_required
def atualizar_usuario(request, pk):
    usuario = get_object_or_404(Usuario, pk=pk)
    if request.method == 'POST':
        form = UsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('listar_usuarios')
    else:
        form = UsuarioForm(instance=usuario)
    return render(request, 'usuarios/atualizar_usuario.html', {'form': form})

@login_required
def deletar_usuario(request, pk):
    usuario = get_object_or_404(Usuario, pk=pk)
    if request.method == 'POST':
        usuario.delete()
        return redirect('listar_usuarios')
    return render(request, 'usuarios/deletar_usuario.html', {'usuario': usuario})

@login_required
def exportar_usuarios_pdf(request):
    # Buscando todos os usuários
    usuarios = Usuario.objects.all()

    # Renderizando o template HTML com os dados dos usuários
    html_string = render_to_string('usuarios/usuarios_pdf.html', {'usuarios': usuarios})

    # Criando a resposta HTTP para o PDF
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="usuarios.pdf"'

    # Convertendo o HTML para PDF usando WeasyPrint
    HTML(string=html_string).write_pdf(response)

    return response