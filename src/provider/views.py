from django.shortcuts import render
from .models import provider

# Create your views here.
def provider (request):
	prov = provider.objects.all()

	return render(request, 'provider/proveedores.html',{'prov':prov})