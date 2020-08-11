from django.shortcuts import render, get_object_or_404, redirect
from products.models import Product
from django.http import HttpResponse
from django.views.generic import View, TemplateView, ListView, UpdateView, CreateView, DeleteView
from .forms import MovForm
from .models import Movement

# Create your views here.


def inventory(request):
	context = {
		'prods' : Product.objects.all(),

	}	
	return render(request, 'movements/inventory.html',context)

def update(request, pk):
	pro = Product.objects.get(id=pk)
	form = MovForm(request.POST)
	if form.is_valid(): 
		mov = form.save()
		mov.prod=pro
		mov.save()
		if mov.entry == 1:
			pro.units += mov.quant
		else:
			pro.units -= mov.quant
			if pro.units < 0 :
				mov.delete()
				return redirect('inventory')
		pro.save()
		return redirect('inventory')

	context = {'form':form}
	return render(request, 'movements/create.html', context)	

class registro(ListView):
	model = Movement
	template_name = 'movements/list.html'
	queryset = Movement.objects.all()