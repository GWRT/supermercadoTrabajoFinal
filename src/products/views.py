from django.shortcuts import render
from .forms import Prod, ProductForm
from .models import Product

# Create your views here.
def products(request):
	form = Prod() #request.GET
	if request.method == "POST":
		form = Prod(request.POST, request.FILES)
		if form.is_valid():
			print(form.cleaned_data)
			Product.objects.create(**form.cleaned_data)
		else:
			print(form.errors)
	context = {
		'form' : form,
	}
	prods = Product.objects.all()
	return render(request,'products.html',{'context':context,'prods':prods})