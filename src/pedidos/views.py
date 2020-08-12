from django.shortcuts import render, redirect
from .form import PedForm
from productos.models import Producto
# Create your views here.

def checkout(request):
	client = request.user.client
	context = {'client':client, 'ped':form}
	if request.method == 'POST':
		ped = form.save()
		ped.client = client

	return render(request, 'pedidos/checkout.html', context)

def pedidos(request, pk):
	pro = Producto.objects.get(id=pk)
	form = PedForm(request.POST)
	if form.is_valid():
		ped = form.save()
		return redirect('checkout')
		
	context = {'pro':pro,'form':form}
	return render(request, 'pedidos/pedido.html', context)	
