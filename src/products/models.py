from django.db import models

# Create your models here.
product_status = [
	(1,"Disponible"),
	(2,"Not disponible"),
]
product_cat = [
	(1,"Category 1"),
	(2,"Category 2"),
	(3,"Category 3"),
]
product_prov = [
	(1,"Prov 1"),
	(2,"Prov 2"),
	(3,"Prov 3"),
]


class Product(models.Model):
	barcode = models.IntegerField()
	name = models.CharField(max_length=20)
	units = models.IntegerField()
	price = models.IntegerField()
	disc = models.IntegerField()
	cat = models.IntegerField(
		null=False, blank=False,
		choices=product_cat,
		default=1,
	)
	prov = models.IntegerField(
		null=False, blank=False,
		choices=product_prov,
		default=1,
	)
	stat = models.IntegerField(
		null=False, blank=False,
		choices=product_status,
		default=1,
	)
	img = models.ImageField(upload_to='pics')

