from django.shortcuts import render
from .forms import SignUpForm
# Create your views here.

def signup(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			raw_password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=raw_password)
			login(request, user)
			return redirect('/')
		else:
			form = SignUpForm()
		return render(request, 'signup.html',{'form':form})


def logout(request):
	auth.logout(request)
	return redirect('/')