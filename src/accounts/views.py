from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib.auth.models import User, auth
# Create your views here.

def signup(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			raw_password = form.cleaned_data.get('password')
			user = auth.authenticate(username=username, password=raw_password)
			signin(request, user)
			return redirect('/')
	else:
		form = SignUpForm()

	return render(request, 'accounts/signup.html',{'form':form})

def signin(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']

		user = auth.authenticate(username=username,password=password)

		if user is not None:
			auth.login(request, user)
			return redirect("/")
		else:
			messages.info(request, 'invalid credentials')
			return redirect('/')

	else:
		return render(request, 'accounts/signin.html')


def logout(request):
	auth.logout(request)
	return redirect('/')