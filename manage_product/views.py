from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpRequest
from django.shortcuts import get_object_or_404, render,redirect
from manage_product.forms import Cerveza_Form, Envase_Form, Categoria_Form, Brew_Form
from manage_product.models import Cerveza, Envase, Categoria, Brew
from users.models import User_profile
from users.forms import User_profile_Form
# Create your views here.

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data= request.POST)

        if form.is_valid():
            username= form.cleaned_data['username']
            password= form.cleaned_data['password']
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                context = {'message':f'Bienvenido {username} al portal'}
                return redirect('index')
            else: 
                context = {'error': 'Usuario o contraseña incorreccto'}
                form = AuthenticationForm()
                return render (request, 'auth/login.html', context=context)
        else:
            errors = form.errors
            form = AuthenticationForm()
            context = {'error':errors, 'form':form}
            return render (request, 'auth/login.html', context=context)
    else:
        form = AuthenticationForm()
        context = {'form':form}
        return render(request,'auth/login.html',context=context)

def register_view(request):
    cervezas = Cerveza.objects.filter(activo=True)
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            context= {'message': f'Usuario {username} creado exitosamente','cervezas':cervezas}
            return render(request, 'index.html', context = context)
        else:
            errors = form.errors
            form = UserCreationForm()
            context = {'errors':errors, 'form': form} 
            return render(request, 'auth/register.html', context=context)
    else:
        form = UserCreationForm
        context = {'form': form}
        return render (request, 'auth/register.html', context = context)


def logout_view(request):
    logout(request)
    return redirect('index')

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
    try:
        perfil= User_profile.objects.get(user=request.user)
    except:
        perfil = None
    context = {
            'cervezas' : cervezas,
            'perfil':perfil,
            }
    return render(request,'gestion_peñon.html',context)

def busqueda_productos_view(request): 
    print(request.GET)
    cervezas = Cerveza.objects.filter(nombre__icontains = request.GET['search'])
    context = {'cervezas':cervezas}
    return render(request, 'busqueda_productos.html', context= context)    

def crear_categoria(request):
    try:
        perfil= User_profile.objects.get(user=request.user)
    except:
        perfil = None
    categorias = Categoria.objects.all()
    if request.method =='GET':
        form = Categoria_Form()
        context = {
        'form':form,
        'categorias':categorias, 
        'perfil':perfil,
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
    try:
        perfil= User_profile.objects.get(user=request.user)
    except:
        perfil = None    
    envases = Envase.objects.all()
    if request.method == 'GET':
        form = Envase_Form()
        context = {
            'form':form,
            'envases': envases,
            'perfil':perfil,
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
    try:
        perfil= User_profile.objects.get(user=request.user)
    except:
        perfil = None    
    brews = Brew.objects.all()
    if request.method == 'GET':
        form = Brew_Form()
        context = {
            'form' : form,
            'brews':brews,
            'perfil':perfil,
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
    try:
        perfil= User_profile.objects.get(user=request.user)
    except:
        perfil = None    
    cervezas = Cerveza.objects.all()
    if request.method=='GET':
        form = Cerveza_Form()
        context = {
        'form' : form,
        'cervezas': cervezas,
        'perfil':perfil,
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
            categoria = get_object_or_404(Categoria,id=pk)
            categoria.delete()
            return redirect('registrar-categoria')

def edit_categoria(request,pk):
    try:
        perfil= User_profile.objects.get(user=request.user)
    except:
        perfil = None    
    categoria = get_object_or_404(Categoria,id=pk)
    if request.method == 'GET':
        categorias = Categoria.objects.all()
        form = Categoria_Form(instance=categoria)
        context = {'form':form,'categorias':categorias,'perfil':perfil}
        return render (request,'edit_categoria.html',context)
    else:
        form = Categoria_Form(request.POST,instance=categoria)
        if form.is_valid():
            categoria.save()
            return redirect('registrar-categoria')

def delete_brew(request,pk):
    brew = get_object_or_404(Brew,id=pk)
    brew.delete()
    return redirect('registrar-brew')

def edit_brew(request,pk):
    try:
        perfil= User_profile.objects.get(user=request.user)
    except:
        perfil = None    
    brew = get_object_or_404(Brew,id=pk)
    if request.method == 'GET':
        brews = Brew.objects.all()
        form = Brew_Form(instance=brew)
        context = {'form':form,'brews':brews,'perfil':perfil}
        return render (request,'edit_brew.html',context)
    else:
        form = Brew_Form(request.POST,instance=brew)
        if form.is_valid():
            brew.save()
            return redirect('registrar-brew')

def delete_envase(request,pk):
    envase = get_object_or_404(Envase,id=pk)
    envase.delete()
    return redirect('registrar-envase')

def edit_envase(request,pk):
    try:
        perfil= User_profile.objects.get(user=request.user)
    except:
        perfil = None    
    envase = get_object_or_404(Envase,id=pk)
    if request.method == 'GET':
        envases = Envase.objects.all()
        form = Envase_Form(instance=envase)
        context = {'form':form,'envases':envases,'perfil':perfil}
        return render (request,'edit_envase.html',context)
    else:
        form = Envase_Form(request.POST,instance=envase)
        if form.is_valid():
            envase.save()
            return redirect('registrar-envase')

def delete_cerveza(request,pk):
    cerveza = get_object_or_404(Cerveza,id=pk)
    cerveza.delete()
    return redirect('registrar-cerveza')

def edit_cerveza(request,pk):
    try:
        perfil= User_profile.objects.get(user=request.user)
    except:
        perfil = None    
    cerveza = get_object_or_404(Cerveza,id=pk)
    if request.method == 'GET':
        cervezas = Cerveza.objects.all()
        form = Cerveza_Form(instance=cerveza)
        context = {'form':form,'cervezas':cervezas,'perfil':perfil}
        return render (request,'edit_cerveza.html',context)
    else:
        form = Cerveza_Form(request.POST,request.FILES,instance=cerveza)
        if form.is_valid():
            cerveza.save()
            return redirect('registrar-cerveza')

def en_construccion(request):
    mensaje='Pagina en Construccion'
    context = {'mensaje':mensaje}
    return render(request,'en_construccion.html',context)

def crear_profile(request):
    if request.method=='GET':
        form = User_profile_Form()
        context = {
        'form' : form,
        }
    else:
        form = User_profile_Form(request.POST, request.FILES)
        if form.is_valid():
            nueva_perfil = User_profile.objects.create(
                    user = request.user,
                    phone = form.cleaned_data['phone'],
                    nombre = form.cleaned_data['nombre'],
                    apellido = form.cleaned_data['apellido'],
                    correo = form.cleaned_data['correo'],
                    profile_image = form.cleaned_data['profile_image']
            )
            return redirect('gestion-peñon')
    return render(request,'auth/crear_profile.html',context)

def edit_profile(request,pk):
    profile = get_object_or_404(User_profile,user=request.user)
    if request.method == 'GET':
        form = User_profile_Form(instance=profile)
        context = {'form':form,'perfil':profile}
        return render (request,'auth/edit_profile.html',context)
    else:
        form = User_profile_Form(request.POST,request.FILES,instance=profile)
        if form.is_valid():
            profile.save()
            return redirect('gestion-peñon')

def eliminar_profile(request,pk):
    profile = get_object_or_404(User_profile,user=request.user)
    if request.method == 'GET':
        mensaje = 'Esta por borrar el perfil'
        form = User_profile_Form(instance=profile)
        context = {'form':form,'mensaje':mensaje}
        return render (request,'auth/del_profile.html',context)
    else:
        profile.delete()
        return redirect('gestion-peñon')
