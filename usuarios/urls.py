from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('',views.listar_usuarios, name="listar_usuarios"),
    path('novo', views.criar_usuario, name="criar_usuario"),
    path('editar/<int:pk>/', views.atualizar_usuario, name='atualizar_usuarios'),
    path('deletar/<int:pk>/', views.deletar_usuario, name='deletar_usuarios'),
    path('exportar_usuarios_pdf/', views.exportar_usuarios_pdf, name='exportar_usuarios_pdf'),

 # URL para a página de login
    path('login/', auth_views.LoginView.as_view(template_name='usuarios/login.html'), name='login'),
    
    # URL para fazer logout
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

]