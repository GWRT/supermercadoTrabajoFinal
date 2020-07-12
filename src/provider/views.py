from django.shortcuts import render
from .models import Provider

# Create your views here.
def providers (request):
	provs = Provider.objects.all()

	return render(request, 'provider/proveedores.html',{'provs':provs})