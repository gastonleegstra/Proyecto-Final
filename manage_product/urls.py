"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path
from manage_product.views import crear_envase, crear_capacidad, crear_cerveza, crear_precio, listar_cervezas,gestion_peñon,index, busqueda_productos_view

urlpatterns = [
    path('', index, name = 'index'),
    path('productos/gestion-peñon', gestion_peñon, name='gestion-peñon'),
    path('productos/registrar-capacidad',crear_capacidad, name='registrar-capacidad'),
    path('productos/registrar-envase',crear_envase, name='registrar-envase'),
    path('productos/registrar-precio', crear_precio, name='registrar-precio'),
    path('productos/registrar-cerveza', crear_cerveza, name='registrar-cerveza'),
    path('productos/listar-cerveza', listar_cervezas, name='listar-cerveza'),
    path('productos/busqueda_productos', busqueda_productos_view, name='busqueda_productos_view'),
]
