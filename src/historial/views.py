from django.shortcuts import render
from .models import History

# Create your views here.
def history(request):
    hist = History.objects.all().order_by('-id')
    context = {
        'historial' : hist
    }
    return render(request, 'historial/historial.html', context)
