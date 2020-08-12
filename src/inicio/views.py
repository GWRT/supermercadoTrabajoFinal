from django.shortcuts import render 
from django.http import JsonResponse
from productos.models import Producto
from django.views.generic import View, TemplateView, ListView, UpdateView, CreateView, DeleteView
import json
from cuentas.models import Client


# Create your views here.

def Inicio(request):
	return render(request, 'Inicio/inicio.html')

def Contactos(request):
	return render(request, 'Inicio/contactos.html')

def Administracion(request):
	return render(request, 'Inicio/administracion.html')

class inventario(ListView):
	model = Producto
	template_name = 'Inicio/inventario.html'
	queryset = Producto.objects.all()

