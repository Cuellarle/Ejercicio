from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from .models import Producto
#from .models import Menu


# Create your views here.
def home(request):
    contexto = {}
    return render(request, "home.html", contexto)

def products(request, ListView=ListView):
    #Obtener todos los producto de la base de datos
    products = Producto.objects.all()
    #Crear un contexto para pasar los productos a la plantilla 
    contexto={'productos':products} 
    return render(request, "productos.html", contexto)
    
def nosotros(request):
    contexto={}
    return render(request, "nosotros.html", contexto)
