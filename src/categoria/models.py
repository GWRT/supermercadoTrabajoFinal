from django.db import models

# Create your models here.
class Category(models.Model):
	name = models.CharField(max_length = 50)
	desc = models.CharField(max_length = 150)

def _str_(self):
		return u'{0}'.format(self.name)