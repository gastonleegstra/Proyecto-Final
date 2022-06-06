from multiprocessing import context
from django.http import HttpRequest
from django.shortcuts import render
from manage_product.forms import Cerveza_Form, Envase_Form, Capacidad_Form, Precio_Form
from manage_product.models import Cerveza

# Create your views here.

def index(request):
    return render(request, 'index.html')

def crear_capacidad(request):
    form = Capacidad_Form()
    context = {
        'form':form
    }
    return render(request,'create_capacidad.html',context)

def crear_envase(request):
    form = Envase_Form()
    context = {
        'form':form
    }
    return render(request,'create_envase.html',context)

def crear_precio(resquest):
    form = Precio_Form()
    context = {
        'form' : form
    }
    return render(resquest,'create_precio.html',context)

def crear_cerveza(resquest):
    form = Cerveza_Form()
    context = {
        'form' : form
    }
    return render(resquest,'create_cerveza.html',context)

def listar_cervezas(resquest):
    cervezas = Cerveza.objects.filter(activo=True)
    context = {
        'cervezas' : cervezas
    }
    return render(resquest,'list_cervezas.html',context)

def gestion_peñon(request):
    cervezas = Cerveza.objects.all()
    context = {
        'cervezas' : cervezas
    }
    return render(request,'gestion_peñon.html',context)

def busqueda_productos_view(request): 
    print(request.GET)
    cervezas = Cerveza.objects.filter(nombre__icontains = request.GET['search'])
    context = {'cervezas':cervezas}
    return render(request, 'busqueda_productos.html', context= context)