from django.shortcuts import render, get_object_or_404, redirect
from products.models import Product
from django.http import HttpResponse
from django.views.generic import View, TemplateView, ListView, UpdateView, CreateView, DeleteView
from .forms import MovForm

# Create your views here.

def inventory(request):
	context = {
		'prods' : Product.objects.all(),
		'form' : MovForm()
	}	
	if request.method == 'POST':
		formulario = MovForm(request.POST, files=request.FILES)
		if formulario.is_valid():
			formulario.save()
			mov = formulario.save(commit=False)
			usuario = request.user
			historial(prod, usuario, 1)
			
			return redirect(to = 'listProduct')
		context['form'] = formulario

	return render(request, 'movements/inventory.html',context)
