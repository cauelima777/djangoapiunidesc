"""
URL configuration for ApiProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from Balconista.views import BalconistaView
from Cliente.views import ClienteView
from Fornecedor.views import FornecedorView
from Livro.views import LivroView
from Pedido.views import PedidoView
from PedidoCliente.views import PedidoClienteView
from PedidoFornecedor.views import PedidoFornecedorView

rotas = routers.DefaultRouter()
rotas.register(r'balconista', BalconistaView, basename='Balconista')
rotas.register(r'cliente', ClienteView, basename='Cliente')
rotas.register(r'fornecedor', FornecedorView, basename='Fornecedor')
rotas.register(r'livro', LivroView, basename='livro')
rotas.register(r'pedido', PedidoView, basename='Pedido')
rotas.register(r'PedidoCliente', PedidoClienteView, basename='PedidoCliente')










urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(rotas.urls))
]
