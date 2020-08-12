from django.db import models
from categorias.models import Categoria
from proveedores.models import Proveedor
from cuentas.models import Client

# Create your models here.

class Producto(models.Model):
	product_status = [
		(1,"Disponible"),
		(2,"Not disponible"),
	]
	barcode = models.IntegerField()
	name = models.CharField(max_length=20)
	price = models.IntegerField()
	cat = models.ForeignKey(Categoria, on_delete = models.SET_NULL, null=True)
	prov = models.ForeignKey(Proveedor, on_delete = models.SET_NULL, null=True)
	stat = models.IntegerField(
		null=False, blank=False,
		choices=product_status,
		default=1,
		)
	img = models.ImageField(upload_to='pics')

	def __str__(self):
		return self.name

class Order(models.Model):
	client = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True, blank=True)
	date_ordered = models.DateTimeField(auto_now_add=True)
	complete = models.BooleanField(default=False, null=True,blank=False)
	transaction_id = models.CharField(max_length=200, null=True)

	def __str__(self):
		return self.id
	
	@property
	def get_cart_total(self):
		orderitem = self.orderitem_set.all()
		total = sum([item.get_total for item in orderitem])
		return total

	@property
	def get_cart_items(self):
		orderitem = self.orderitem_set.all()
		total = sum([item.quantity for item in orderitem])
		return total


class OrderItem(models.Model):
	product = models.ForeignKey(Producto, on_delete=models.SET_NULL, null=True, blank=True)
	order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, blank=True)
	quantity = models.IntegerField(default=0,null=True, blank=True)
	date_added = models.DateTimeField(auto_now_add=True)

	@property
	def get_total(self):
		total = self.quantity * self.product.price
		return total

