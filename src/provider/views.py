from django.shortcuts import render
from .models import Provider

# Create your views here.
def providers (request):
	prov = Provider.objects.all()

	return render(request, 'provider/proveedores.html',{'prov':prov})