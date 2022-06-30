from multiprocessing import context
import re
from urllib import request
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpRequest
from django.shortcuts import render,redirect
from manage_product.forms import Cerveza_Form, Envase_Form, Capacidad_Form, Precio_Form
from manage_product.models import Capacidad, Cerveza, Precio, Envase

# Create your views here.

def login_view(request):
    if request.method == 'POST':
        pass

    else:
        form = AuthenticationForm()
        context = {'form':form}
        return render(request,'auth/login.html',context=context)



def index(request):
    cervezas = Cerveza.objects.filter(activo=True)
    context = {
        'cervezas' : cervezas
    }
    return render(request, 'index.html',context)

def crear_capacidad(request):
    capacidades = Capacidad.objects.all()
    if request.method =='GET':
        form = Capacidad_Form()
        context = {
        'form':form,
        'capacidades':capacidades, 
        }
    else:
        form = Capacidad_Form(request.POST)
        if form.is_valid():
            nueva_capacidad = Capacidad.objects.create(
                volumen = form.cleaned_data['volumen'],
                medida = form.cleaned_data['medida'],
                activo = form.cleaned_data['activo'],
            )
            capacidades = Capacidad.objects.all()
            form = Capacidad_Form()
            context = {
                'form':form,
                'capacidades':capacidades, 
            }
    return render(request,'create_capacidad.html',context)

def crear_envase(request):
    envases = Envase.objects.all()
    if request.method == 'GET':
        form = Envase_Form()
        context = {
            'form':form,
            'envases': envases,
        }
    else:
        form = Envase_Form(request.POST)
        if form.is_valid():
            nuevo_envase = Envase.objects.create(
                tipo = form.cleaned_data['tipo'],
                capacidad = form.cleaned_data['capacidad'],
                activo = form.cleaned_data['activo'],
            )
        envases = Envase.objects.all()
        form = Envase_Form()
        context = {
            'form':form,
            'envases': envases,
        }    
    return render(request,'create_envase.html',context)

def crear_precio(request):
    precios = Precio.objects.all()
    if request.method == 'GET':
        form = Precio_Form()
        context = {
            'form' : form,
            'precios':precios,
        }
    else:
        form=Precio_Form(request.POST)
        if form.is_valid():
            nuevo_precio = Precio.objects.create(
                    precio = form.cleaned_data['precio'],
                    fecha_alta = form.cleaned_data['fecha_alta'],
                    activo =form.cleaned_data['activo'],
                )
            precios = Precio.objects.all()
            form = Precio_Form()
            context = {
                'form':form,
                'precios':precios,
            }
    return render(request,'create_precio.html',context)

def crear_cerveza(request):
    cervezas = Cerveza.objects.all()
    if request.method=='GET':
        form = Cerveza_Form()
        context = {
        'form' : form,
        'cervezas': cervezas,
        }
    else:
        form = Cerveza_Form(request.POST)
        if form.is_valid():
            nueva_cerveza = Cerveza.objects.create(
                nombre = form.cleaned_data['nombre'],
                descripcion = form.cleaned_data['descripcion'],
                abv = form.cleaned_data['abv'],
                ibu = form.cleaned_data['ibu'],
                precio = form.cleaned_data['precio'],
                brew =form.cleaned_data['brew'],
                color = form.cleaned_data['color'],
                envase = form.cleaned_data['envase'],
                activo = form.cleaned_data['activo'],
            )
            cervezas = Cerveza.objects.all()
            form = Cerveza_Form()
            context = {
            'form' : form,
            'cervezas':cervezas,
            }  
    return render(request,'create_cerveza.html',context)

def listar_cervezas(request):
    cervezas = Cerveza.objects.filter(activo=True)
    context = {
        'cervezas' : cervezas
    }
    return render(request,'list_cervezas.html',context)

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




