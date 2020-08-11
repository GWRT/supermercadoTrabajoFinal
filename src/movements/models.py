from django.db import models
from django.contrib.auth.models import User
from products.models import Product

# Create your models here.
 
type_entry = [
    (1, "Entrada"),
    (2, "Salida"),
]
class Movement(models.Model):
    prod = models.ForeignKey(Product, on_delete = models.SET_NULL, null=True)
    entry = models.IntegerField(
        null=False, blank=False,
		choices=type_entry,
		default=1,
    )
    quant = models.IntegerField()
