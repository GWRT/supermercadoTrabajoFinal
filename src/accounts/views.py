from django.shortcuts import render, redirect
from .forms import AccountForm, UpdateForm, AccountUpdate
from .models import Account
from django.contrib.auth.models import User, auth
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash

# Create your views here.
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

	context = {
	'form' : form,
	}
	return render(request, 'accounts/password.html', context)
