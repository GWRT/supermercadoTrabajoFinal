from django.shortcuts import render 
from django.http import JsonResponse
from productos.models import Producto
from django.views.generic import View, TemplateView, ListView, UpdateView, CreateView, DeleteView
import json
from productos.models import Order, OrderItem
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

def checkout(request):
	if request.user.is_authenticated:
		client = request.user.client
		order, created = Order.objects.get_or_create(client=client, complete=False)
		items = order.orderitem_set.all()
		cartItems = order.get_cart_items
	else:
		items = []
		order = {'get_cart_total':0,'get_cart_items':0}
		cartItems = order['get_cart_items']

	context = {'items':items, 'order':order, 'cartItems':cartItems}
	return render(request, 'Inicio/checkout.html', context)

def update_item(request):
	data =json.loads(request.body)
	productId = data['productId']
	action = data['action']
	print('action:',action)
	print('productId:', productId)

	client = request.user.client
	product = Producto.objects.get(id=productId)
	order, created = Order.objects.get_or_create(client=client, complete=False)
	orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)
	
	if action == 'add':
		orderItem.quantity = (orderItem.quantity +1)
	elif action == 'remove':
		orderItem.quantity = (orderItem.quantity -1)

	orderItem.save()

	if orderItem.quantity <= 0:
		orderItem.delete()

	return JsonResponse('item was added', safe=False)

def cart(request):
	if request.user.is_authenticated:
		client = request.user.client
		order, created = Order.objects.get_or_create(client=client, complete=False)
		items = order.orderitem_set.all()
		cartItems = order.get_cart_items
	else:
		items = []
		order = {'get_cart_total':0,'get_cart_items':0}
		cartItems = order['get_cart_items']

	context = {'items':items, 'order':order, 'cartItems':cartItems}
	return render(request, 'Inicio/Cart.html', context)