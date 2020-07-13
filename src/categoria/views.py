from django.shortcuts import render
from .models import Category

# Create your views here.
def categories(request):
	cats = Category.objects.all()

	return render(request, 'categoria/categorias.html', {'cats':cats})

def crearCategoria(request):
	return render(request, 'categoria/categorias.html', {})	

def modificarCategoria(request, id):
	return render(request, 'categoria/categorias.html', {})	

def eliminarCategoria(request, id):
	return render(request, 'categoria/categorias.html', {})			