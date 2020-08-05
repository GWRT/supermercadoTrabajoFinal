from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth

# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username = username, password = password)

        if user is not None:
            if user.is_superuser:
                auth.login(request, user)
                return redirect('homePage')
            else:
                messages.info(request, 'La cuenta no es superusuario')
                return redirect('login')
        else:
            messages.info(request, 'La cuenta no existe')
            return redirect('login')
    else:
        return render(request, 'accounts/login.html')