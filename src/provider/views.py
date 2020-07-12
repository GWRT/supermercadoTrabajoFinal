from django.shortcuts import render
from .models import Provider
from .forms import providerForm

# Create your views here.
def providers (request):
	provs = Provider.objects.all()

	return render(request, 'provider/proveedores.html',{'provs':provs})

def modificar(request, id):
	provs = Provider.objects.get(id = id)

	if request.method == 'POST':
		form = 	providerForm(data=request.POST, instance=provs)

		if form.is_valid():
			form.save()
			return redirect(to='providers')

	return render(request, 'provider/modificar.html',{'form':providerForm(instance=provs)})		