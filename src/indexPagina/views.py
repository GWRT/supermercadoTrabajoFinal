from django.shortcuts import render
from categoria.models import Category
from provider.models import Provider
from products.models import Product
from django.contrib.auth.models import User
# Create your views here.
def home(request):
	countC = Category.objects.all().count()
	countP = Provider.objects.all().count()
	countR = Product.objects.all().count()
	countA = User.objects.all().count()
	context = {'countA':countA, 'countC':countC, 'countP':countP, 'countR': countR}
	return render(request, 'indexPagina/titles.html', context)