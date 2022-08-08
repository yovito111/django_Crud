from django.shortcuts import render, redirect
from .models import Producto
from .forms import ProductForm
# Create your views here.

def inicio(request):
    return render(request, 'paginas/inicio.html')

def nosotros(request):
    return render(request,'paginas/nosotros.html')

def productos(request):
    productos = Producto.objects.all()
    return render(request, 'productos/index.html', {'productos': productos})

def crear_producto(request):
    formulario = ProductForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('productos')
    return render(request, 'productos/crear.html', {'formulario' : formulario})

def editar(request, id):
    productos = Producto.objects.get(id=id)
    formulario = ProductForm(request.POST or None, request.FILES or None, instance=productos)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('productos')
    return render(request, 'productos/editar.html', {'formulario' : formulario})

def borrar(request, id):
    productos = Producto.objects.get(id=id)
    productos.delete()
    return redirect ('productos')