from django.shortcuts import render
from categoria.models import Category
from provider.models import Provider
from products.models import Product
# Create your views here.
def home(request):
	countC = Category.objects.all().count()
	countP = Provider.objects.all().count()
	countR = Product.objects.all().count()
	context = {'countC':countC, 'countP':countP, 'countR': countR}
	return render(request, 'indexPagina/titles.html', context)