
from django.contrib import admin
from django.urls import path, include

from venda.views import listar_produtos

urlpatterns = [
    path('admin/', admin.site.urls),
    path('venda/', include('venda.urls')),
    path('usuarios/', include('usuarios.urls')),
    path('',listar_produtos, name="listar_produtos"),
]
