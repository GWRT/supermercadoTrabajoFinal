from django.shortcuts import render, redirect
from .models import Provider
from .forms import providerForm

# Create your views here.
def providers (request):
	context = {
		'provs' : Provider.objects.all(),
	}	
	return render(request, 'provider/proveedores.html',context)

def create(request):
	context = {
		'form' : providerForm()
	}

	if request.method == 'POST':
		formulario = providerForm(request.POST)
		if formulario.is_valid():
			formulario.save()
			print('guardado')
			return redirect(to = 'provider')
		context['form'] = formulario

	return render(request, 'provider/create.html', context)	

def modificar(request, id):
	provs = Provider.objects.get(id = id)

	if request.method == 'POST':
		form = 	providerForm(data=request.POST, instance=provs)

		if form.is_valid():
			form.save()
			return redirect('provider')

	return render(request, 'provider/modificar.html',{'form':providerForm(instance=provs)})		


def eliminar(request, id):
	provs = Provider.objects.get(id = id)
	provs.delete()

	return redirect(to='provider')