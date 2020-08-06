from django.shortcuts import render
from .models import History

# Create your views here.
def historial(request, Prod, Usuario):
    History.objects.create(prod = Prod, )
