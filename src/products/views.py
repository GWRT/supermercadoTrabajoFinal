from django.shortcuts import render, redirect
from .forms import ProductForm
from .models import Product
from django.http import HttpResponse
from django.views.generic import View
from .utils import render_to_pdf
from historial.utils import historial

# Create your views here.
def listProduct(request):
	context = {
		'prods' : Product.objects.all(),
	}	
	return render(request, 'products/products.html',context)

def addProduct(request):
	context = {
		'form' : ProductForm()
	}

	if request.method == 'POST':
		formulario = ProductForm(request.POST)
		if formulario.is_valid():
			prod = formulario.save(commit=False)
			usuario = request.user
			historial(prod, usuario, 1)
			prod.save()
			return redirect(to = 'listProduct')
		context['form'] = formulario

	return render(request, 'products/add.html', context)	

def deleteProduct(request, id):
	prod = Product.objects.get(id = id)
	usuario = request.user
	historial(prod, usuario, 2)
	prod.delete()

	return redirect(to='listProduct')

def updateProduct(request, id):
	prod = Product.objects.get(id = id)

	if request.method == 'POST':
		form = ProductForm(data=request.POST, instance=prod)

		if form.is_valid():
			producto = form.save(commit=False)
			usuario = request.user
			historial(producto, usuario, 3)
			return redirect('listProduct')

	return render(request, 'products/update.html',{'form':ProductForm(instance=prod)})

class listProductPDF(View):
	def get(self, request, *args, **kwargs):
		products = Product.objects.all()
		data = {
			'products' : products
		}
		pdf = render_to_pdf('products/tablaProductos.html', data)
		return HttpResponse(pdf, content_type = 'application/pdf')
