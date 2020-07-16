from django.db import models

# Create your models here.
class Provider(models.Model):
	ruc = models.IntegerField()
	razonSocial = models.CharField(max_length = 100)
	persona = models.CharField(max_length = 100)
	direccion = models.CharField(max_length = 200)
	email = models.EmailField(max_length = 254)
	telefono = models.IntegerField()
	estado =  models.BooleanField(default = True)
	def __str__(self):
		return str(self.persona)