from django.db import models

# Create your models here.
class Provider(models.Model):
	ruc = models.IntegerField()
	razonSocial = models.CharField(max_length = 100)
	nombre = models.CharField()
	direccion = models.CharField()
	celular = models.IntegerField()
	ciudad = models.CharField()
