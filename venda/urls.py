
from django.urls import path
from . import views

urlpatterns = [

    path('produtos', views.listar_produtos, name='listar_produtos'),
    path('produtos/novo/', views.criar_produto, name='criar_produto'),
    path('produtos/editar/<int:id>/', views.atualizar_produto, name='atualizar_produto'),
    path('produtos/deletar/<int:id>/', views.deletar_produto, name='deletar_produto'),
    path('exportar_produtos_pdf/', views.exportar_produtos_pdf, name='exportar_produtos_pdf'),

    path('clientes',views.listar_clientes, name="listar_clientes"),
    path('novo', views.criar_cliente, name="criar_clientes"),
    path('editar/<int:id>/', views.atualizar_cliente, name='atualizar_cliente'),
    path('deletar/<int:id>/', views.deletar_cliente, name='deletar_cliente'),
    path('exportar_clientes_pdf/', views.exportar_clientes_pdf, name='exportar_clientes_pdf'),

    path('estoques',views.listar_estoques, name="listar_estoques"),
    path('estoques/novo/', views.criar_estoque, name='criar_estoque'),
    path('estoques/editar/<int:id>/', views.atualizar_estoque, name='atualizar_estoque'),
    path('estoques/deletar/<int:id>/', views.deletar_estoque, name='deletar_estoque'),
    path('exportar_estoque_pdf/', views.exportar_estoque_pdf, name='exportar_estoque_pdf'),
]