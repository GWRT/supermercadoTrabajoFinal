from django.db import models
from productos.models import Producto
from cuentas.models import Client

# Create your models here.

class Pedido(models.Model):
	user = models.ForeignKey(Client, on_delete=models.CASCADE)
	item = models.ForeignKey(Producto, on_delete=models.CASCADE)
	quantity = models.IntegerField(default=1)

	def __str__(self):
		return f"{self.quantity} of {self.item.title}"

	def get_price(self):
		return self.quantity * self.item.price
