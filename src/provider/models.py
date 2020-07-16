from django.db import models

# Create your models here.
class Provider(models.Model):
	ruc = models.IntegerField()
	razonSocial = models.CharField(max_length = 100)
	persona = models.CharField(max_length = 100)
	direccion = models.CharField(max_length = 200)
	email = models.EmailField(max_length = 254)
	telefono = models.IntegerField()
<<<<<<< HEAD
	estado =  models.BooleanField(default = True)
	def __str__(self):
		return str(self.persona)
=======
	estado =  models.BooleanField(default = True)
>>>>>>> 4786988726fc999a50ea59034cd580e9df6ee5c7
