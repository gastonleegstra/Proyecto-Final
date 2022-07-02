from email.mime import image
from urllib import request
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpRequest
from django.shortcuts import render,redirect
from manage_product.forms import Cerveza_Form, Envase_Form, Categoria_Form, Brew_Form
from manage_product.models import Cerveza, Envase, Categoria, Brew
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

def crear_categoria(request):
    categorias = Categoria.objects.all()
    if request.method =='GET':
        form = Categoria_Form()
        context = {
        'form':form,
        'categorias':categorias, 
        }
    else:
        form = Categoria_Form(request.POST)
        if form.is_valid():
            nueva_categoria = Categoria.objects.create(
                categoria = form.cleaned_data['categoria'],
                descripcion = form.cleaned_data['descripcion'],
                activo = form.cleaned_data['activo'],
            )
            categorias = Categoria.objects.all()
            form = Categoria_Form()
            context = {
                'form':form,
                'categorias':categorias, 
            }
    return render(request,'create_categoria.html',context)

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
                volumen = form.cleaned_data['volumen'],
                medida = form.cleaned_data['medida'],
                activo = form.cleaned_data['activo'],
            )
        envases = Envase.objects.all()
        form = Envase_Form()
        context = {
            'form':form,
            'envases': envases,
        }    
    return render(request,'create_envase.html',context)

def crear_brew(request):
    brews = Brew.objects.all()
    if request.method == 'GET':
        form = Brew_Form()
        context = {
            'form' : form,
            'brews':brews,
        }
    else:
        form=Brew_Form(request.POST)
        if form.is_valid():
            nuevo_brew = Brew.objects.create(
                    elaborador = form.cleaned_data['elaborador'],
                    descripcion = form.cleaned_data['descripcion'],
                    activo =form.cleaned_data['activo'],
                )
            brews = Brew.objects.all()
            form = Brew_Form()
            context = {
                'form':form,
                'brews':brews,
            }
    return render(request,'create_brew.html',context)

def crear_cerveza(request):
    cervezas = Cerveza.objects.all()
    if request.method=='GET':
        form = Cerveza_Form()
        context = {
        'form' : form,
        'cervezas': cervezas,
        }
    else:
        form = Cerveza_Form(request.POST, request.FILES)
        if form.is_valid():
            nueva_cerveza = Cerveza.objects.create(
                nombre = form.cleaned_data['nombre'],
                descripcion = form.cleaned_data['descripcion'],
                abv = form.cleaned_data['abv'],
                ibu = form.cleaned_data['ibu'],
                precio = form.cleaned_data['precio'],
                tipo =form.cleaned_data['tipo'],
                brew =form.cleaned_data['brew'],
                color = form.cleaned_data['color'],
                envase = form.cleaned_data['envase'],
                categoria =form.cleaned_data['categoria'],
                image =form.cleaned_data['image'],
                activo = form.cleaned_data['activo'],
            )
            cervezas = Cerveza.objects.all()
            form = Cerveza_Form()
            context = {
            'form' : form,
            'cervezas':cervezas,
            }  
    return render(request,'create_cerveza.html',context)

def delete_categoria(request,pk):
            categoria = Categoria.objects.get(id=pk)
            categoria.delete()
            return redirect('registrar-categoria')

def edit_categoria(request,pk):
    categoria = Categoria.objects.get(id=pk)
    if request.method == 'GET':
        categorias = Categoria.objects.all()
        form = Categoria_Form(instance=categoria)
        context = {'form':form,'categorias':categorias}
        return render (request,'edit_categoria.html',context)
    else:
        form = Categoria_Form(request.POST,instance=categoria)
        if form.is_valid():
            categoria.save()
            return redirect('registrar-categoria')

def delete_brew(request,pk):
            brew = Brew.objects.get(id=pk)
            brew.delete()
            return redirect('registrar-brew')

def edit_brew(request,pk):
    brew = Brew.objects.get(id=pk)
    if request.method == 'GET':
        brews = Brew.objects.all()
        form = Brew_Form(instance=brew)
        context = {'form':form,'brews':brews}
        return render (request,'edit_brew.html',context)
    else:
        form = Brew_Form(request.POST,instance=brew)
        if form.is_valid():
            brew.save()
            return redirect('registrar-brew')

def delete_envase(request,pk):
            envase = Envase.objects.get(id=pk)
            envase.delete()
            return redirect('registrar-envase')

def edit_envase(request,pk):
    envase = Envase.objects.get(id=pk)
    if request.method == 'GET':
        envases = Envase.objects.all()
        form = Envase_Form(instance=envase)
        context = {'form':form,'envases':envases}
        return render (request,'edit_envase.html',context)
    else:
        form = Envase_Form(request.POST,instance=envase)
        if form.is_valid():
            envase.save()
            return redirect('registrar-envase')

def delete_cerveza(request,pk):
            cerveza = Cerveza.objects.get(id=pk)
            cerveza.delete()
            return redirect('registrar-cerveza')

def edit_cerveza(request,pk):
    cerveza = Cerveza.objects.get(id=pk)
    if request.method == 'GET':
        cervezas = Cerveza.objects.all()
        form = Cerveza_Form(instance=cerveza)
        context = {'form':form,'cervezas':cervezas}
        return render (request,'edit_cerveza.html',context)
    else:
        form = Cerveza_Form(request.POST,request.FILES,instance=cerveza)
        if form.is_valid():
            cerveza.save()
            return redirect('registrar-cerveza')
