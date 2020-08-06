from django.shortcuts import render, redirect
from .forms import AccountForm
from .models import Account
from django.contrib.auth.models import User, auth
# Create your views here.
<<<<<<< HEAD
def account(request):
    return render(request, 'accounts/account.html')

def update(request):
    account = Account.objects.get(id=request.user.id)
    form = AccountForm(instance=account)
    if request.method == 'POST':
        form = AccountForm(request.POST, request.FILES)
        if forms.is_valid():
            forms.save() 
    context = {'form': form}
    return render(request, 'accounts/update.html', context)
=======

def signup(request):
	context = {
		'formulario' : SignUpForm()
	}
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			raw_password = form.cleaned_data.get('password')
			user = auth.authenticate(username=username, password=raw_password)
			auth.login(request, user)
			return redirect(to = 'homePage')
		context['formulario'] = form

	return render(request, 'accounts/signup.html',context)

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
			return redirect('signin')

	else:
		return render(request, 'accounts/signin.html')


def logout(request):
	auth.logout(request)
	return redirect('/')
>>>>>>> 459d354b9c2272a5fc640cded2edff0c46bcfa03
