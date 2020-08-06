from django.db import models
from django.contrib.auth.models import User
from products.models import Product

# Create your models here.

type_entry = [
    (1, "Ingresar"),
    (2, "Eliminar"),
]
class History(models.Model):
    prod = models.ForeignKey(Product, on_delete = models.CASCADE)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    date = models.DateTimeField(auto_now=True)
    entry = models.IntegerField(
        null=False, blank=False,
		choices=type_entry,
		default=1,
    )