from django.db import models

# Create your models here.
class Category(models.Model):
	name = models.CharField(max_length = 50)
<<<<<<< HEAD
	desc = models.CharField(max_length = 150)
	
	def __str__(self):
		return self.name
=======
	desc = models.CharField(max_length = 150)
>>>>>>> 4786988726fc999a50ea59034cd580e9df6ee5c7
