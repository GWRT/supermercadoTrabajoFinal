from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from .forms import LoginForm, SignUpForm
from accounts.models import Account

# Create your views here.
def login(request):
	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			user = auth.authenticate(username=username, password=password)
			if user is not None:
				auth.login(request, user)
				return redirect('/home')

	else:
		form = LoginForm()			

	context = {'form': form}
	return render(request, 'administrators/login.html', context)

def signup(request):
	form = SignUpForm()
	if request.method == 'POST':
		form = SignUpForm(request.POST)  
		if form.is_valid():
			form.save()
			return redirect('/')
			
	context = {'form': form}
	return render(request, 'administrators/signup.html', context)

def logout(request):
	auth.logout(request)
	return redirect('/')