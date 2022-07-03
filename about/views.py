from multiprocessing import context
from django.shortcuts import render
from about.models import Developer

# Create your views here.
def about(request):
    developers = Developer.objects.all()
    context = {
        'developers':developers
    }
    return render(request,'about/about.html',context)