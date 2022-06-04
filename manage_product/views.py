from multiprocessing import context
from django.http import HttpRequest
from django.shortcuts import render
from manage_product.forms import Cerveza_Form, Envase_Form, Capacidad_Form, Precio_Form

# Create your views here.
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