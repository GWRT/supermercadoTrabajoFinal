from django.shortcuts import render, get_object_or_404, redirect
from .forms import ProductForm
from .models import Product
from django.http import HttpResponse
from django.views.generic import View, TemplateView, ListView, UpdateView, CreateView, DeleteView
from django.urls import reverse_lazy
from .utils import render_to_pdf

# Create your views here.
class listProduct(ListView):
	model = Product
	template_name = 'products/products.html'
	queryset = Product.objects.all()

class addProduct(CreateView):
	model = Product
	template_name = 'products/add.html'
	form_class = ProductForm
	success_url = reverse_lazy('listProduct')

class deleteProduct(DeleteView):
	model = Product
	success_url = reverse_lazy('listProduct')

class updateProduct(UpdateView):
	model = Product
	template_name = 'products/update.html'
	form_class = ProductForm
	success_url = reverse_lazy('listProduct')

class listProductPDF(View):
	def get(self, request, *args, **kwargs):
		products = Product.objects.all()
		data = {
			'products' : products
		}
		pdf = render_to_pdf('products/tablaProductos.html', data)
		return HttpResponse(pdf, content_type = 'application/pdf')
<<<<<<< HEAD

=======
>>>>>>> 459d354b9c2272a5fc640cded2edff0c46bcfa03
