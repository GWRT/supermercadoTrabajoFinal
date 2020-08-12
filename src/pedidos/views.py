from django.shortcuts import render, redirect
from .form import PedForm
from productos.models import Producto
from .models import Pedido, Venta

# Create your views here.

def checkout(request, pk):
	ped = Pedido.objects.get(id=pk)
	context = {'ped':ped}
	if request.method == 'POST':
		ven = Venta.objects.create()
		ven.ped = ped
		pro = ped.item
		pro.units -= ped.quantity
		return redirect('Inicio')

	return render(request, 'pedidos/checkout.html', context)

def pedidos(request, pk):
	pro = Producto.objects.get(id=pk)
	form = PedForm(request.POST)
	if form.is_valid():
		ped = form.save()
		ped.user = request.user.client
		ped.item = pro
		print(ped.id)
		ped.save()
		
		
	context = {'pro':pro,'form':form}
	return render(request, 'pedidos/pedido.html', context)	
