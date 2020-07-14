from django.db import models

# Create your models here.
class Product(models.Model):
	barcode = models.IntegerField()
	name = models.CharField(max_length=20)
	units = models.IntegerField()
	price = models.IntegerField()
	img = models.ImageField(upload_to='pics')

