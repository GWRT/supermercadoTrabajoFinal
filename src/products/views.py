from django.shortcuts import render, get_object_or_404, redirect
from .forms import ProductForm
from .models import Product
from django.views.generic import View, TemplateView, ListView, UpdateView, CreateView, DeleteView
from django.urls import reverse_lazy

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

class productsList(ListView):
	model = Product
	template_name = 'products/tablaProductos.html'
	context_object_name = 'products'

class ListView	