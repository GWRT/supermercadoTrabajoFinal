from django.db import models
from categoria.models import Category
from provider.models import Provider

# Create your models here.
product_status = [
	(1,"Disponible"),
	(2,"Not disponible"),
]

class Product(models.Model):
	barcode = models.IntegerField()
	name = models.CharField(max_length=20)
	units = models.IntegerField()
	price = models.IntegerField()
	disc = models.IntegerField()
	cat = models.ForeignKey(Category, on_delete = models.SET_NULL, null=True)
	prov = models.ForeignKey(Provider, on_delete = models.SET_NULL, null=True)
	stat = models.IntegerField(
		null=False, blank=False,
		choices=product_status,
		default=1,
	)
	img = models.ImageField(upload_to='pics')

	def __str__(self):
		return self.name

