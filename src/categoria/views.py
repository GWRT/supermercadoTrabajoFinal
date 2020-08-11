from django.shortcuts import render, redirect
from .models import Category
from .forms import categoryForm

# Create your views here.
def categories(request):
	cats = Category.objects.all()

	return render(request, 'categoria/categorias.html', {'cats':cats})

def crearCategoria(request):
	context = {
		'form' : categoryForm()
	}

	if request.method == 'POST':
		formulario = categoryForm(request.POST)
		if formulario.is_valid():
			formulario.save()
			return redirect(to = 'category')

		context['form'] = formulario

	return render(request, 'categoria/create.html', context)	

def modificarCategoria(request, id):
	cats = Category.objects.get(id = id)

	if request.method == 'POST':
		form = 	categoryForm(data=request.POST, instance=cats)

		if form.is_valid():
			form.save()
			return redirect('category')

	return render(request, 'categoria/modificar.html',{'form':categoryForm(instance=cats)})

def eliminarCategoria(request, id):
	cats = Category.objects.get(id = id)
	cats.delete()

	return redirect(to='category')			