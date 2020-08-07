from django.shortcuts import render, redirect
from .forms import AccountForm, UpdateForm, AccountUpdate
from .models import Account
from django.contrib.auth.models import User, auth
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash

# Create your views here.
<<<<<<< HEAD
def account(request):
	if request.method == 'POST':
		u_form = UpdateForm(request.POST, instance=request.user)
		a_form = AccountUpdate(request.POST, request.FILES, instance=request.user.account)
		if u_form.is_valid() and a_form.is_valid:
			u_form.save()
			a_form.save()
			return redirect('account')
	else: 
		u_form = UpdateForm(instance=request.user)
		a_form = AccountUpdate(instance=request.user.account)

	context = {
	'u_form' : u_form,
	'a_form' : a_form,
	}
	return render(request, 'accounts/account.html', context)

def cpassword(request):
	if request.method == 'POST':
		form = PasswordChangeForm(data=request.POST, user=request.user)
		if form.is_valid():
			form.save()
			update_session_auth_hash(request, form.user)
			return redirect('account')

		else:
			return redirect('account')
	else: 
		form = PasswordChangeForm(user=request.user)

<<<<<<< HEAD
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
=======
	context = {
	'form' : form,
	}
	return render(request, 'accounts/password.html', context)
>>>>>>> rama2
