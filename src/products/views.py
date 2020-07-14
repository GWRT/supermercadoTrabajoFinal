from django.shortcuts import render, get_object_or_404, redirect
from .forms import Prod, ProductForm
from .models import Product

# Create your views here.
def products(request):
	prods = Product.objects.all()
	return render(request,'products.html',{'prods': prods})

def addProduct(request):
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
	return render(request,'form.html',context)

def updateProduct(request,theid):
	obj = Product.objects.get(id = theid)
	form = ProductForm(request.POST or None,  instance = obj)
	if form.is_valid():
		if bool(request.FILES.get('img',False)) == True:
			obj.img = request.FILES['img']
		form.save()
		form = ProductForm()
	context = {
		'form': form,
	}
	return render(request, "form.html", context)

def deleteProduct(request,theid):
	obj = get_object_or_404(Product, id = theid)
	if request.method == 'POST':
		print("Lo borro")
		obj.delete()
	context = {
		'obj': obj,
	}
	return render(request, "delete.html", context)
