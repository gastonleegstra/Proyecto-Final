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
from manage_product.views import crear_envase, crear_categoria, crear_cerveza, crear_brew, listar_cervezas,gestion_peñon,index, busqueda_productos_view, login_view,delete_categoria,edit_categoria,edit_brew,delete_brew,delete_envase,edit_envase,delete_cerveza,edit_cerveza,logout_view, register_view, edit_profile,crear_profile,eliminar_profile
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', index, name = 'index'),
    path('productos/gestion-peñon', gestion_peñon, name='gestion-peñon'),
    path('productos/registrar-categoria',crear_categoria, name='registrar-categoria'),
    path('productos/delete-categoria/<int:pk>/', delete_categoria, name = 'delete-categoria'),
    path('productos/edit-categoria/<int:pk>/', edit_categoria, name = 'edit-categoria'),
    path('productos/registrar-envase',crear_envase, name='registrar-envase'),
    path('productos/delete-envase/<int:pk>/', delete_envase, name = 'delete-envase'),
    path('productos/edit-envase/<int:pk>/', edit_envase, name = 'edit-envase'),
    path('productos/registrar-brew', crear_brew, name='registrar-brew'),
    path('productos/delete-brew/<int:pk>/', delete_brew, name = 'delete-brew'),
    path('productos/edit-brew/<int:pk>/', edit_brew, name = 'edit-brew'),
    path('productos/registrar-cerveza', crear_cerveza, name='registrar-cerveza'),
    path('productos/delete-cerveza/<int:pk>/', delete_cerveza, name = 'delete-cerveza'),
    path('productos/edit-cerveza/<int:pk>/', edit_cerveza, name = 'edit-cerveza'),
    path('productos/listar-cerveza', listar_cervezas, name='listar-cerveza'),
    path('productos/busqueda_productos', busqueda_productos_view, name='busqueda_productos_view'),
    path('accounts/login', login_view, name='login'),
    path('accounts/logout', logout_view, name='logout'),
    path('accounts/register', register_view, name='register'),
    path('accounts/crear-profile/', crear_profile, name='crear-profile'),
    path('accounts/edit-profile/<int:pk>/', edit_profile, name='edit-profile'),
    path('accounts/eliminar-profile/<int:pk>/', eliminar_profile, name='eliminar-profile'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
