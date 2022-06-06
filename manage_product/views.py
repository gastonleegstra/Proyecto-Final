from multiprocessing import context
from django.http import HttpRequest
from django.shortcuts import render
from manage_product.forms import Cerveza_Form, Envase_Form, Capacidad_Form, Precio_Form
from manage_product.models import Capacidad, Cerveza, Precio, Envase

# Create your views here.

def index(request):
    return render(request, 'index.html')

def crear_capacidad(request):
    if request.method =='GET':
        estado=0
        form = Capacidad_Form()
        context = {
        'form':form
        }
    else:
        estado=1
        form = Capacidad_Form(request.POST)
        if form.is_valid():
            estado=2
            nueva_capacidad = Capacidad.objects.create(
                volumen = form.cleaned_data['volumen'],
                medida = form.cleaned_data['medida'],
                activo = form.cleaned_data['activo'],
            )
            form = Capacidad_Form()
            context = {
                'form':form,
                'estado':estado
            }
    return render(request,'create_capacidad.html',context)

def crear_envase(request):
    if request.method == 'GET':
        form = Envase_Form()
        context = {
            'form':form
        }
    else:
        form = Envase_Form(request.POST)
        if form.is_valid():
            nuevo_envase = Envase.objects.create(
                tipo = form.cleaned_data['tipo'],
                capacidad = form.cleaned_data['capacidad'],
                activo = form.cleaned_data['activo'],
            )
        form = Envase_Form()
        context = {
            'form':form
        }    
    return render(request,'create_envase.html',context)

def crear_precio(request):
    if request.method == 'GET':
        form = Precio_Form()
        context = {
            'form' : form
        }
    else:
        form=Precio_Form(request.POST)
        if form.is_valid():
            nuevo_precio = Precio.objects.create(
                    precio = form.cleaned_data['precio'],
                    fecha_alta = form.cleaned_data['fecha_alta'],
                    activo =form.cleaned_data['activo'],
                )
            form = Precio_Form()
            context = {
                'form':form,
            }
    return render(request,'create_precio.html',context)

def crear_cerveza(request):
    if request.method=='GET':
        form = Cerveza_Form()
        context = {
        'form' : form
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
            form = Cerveza_Form()
            context = {
            'form' : form
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