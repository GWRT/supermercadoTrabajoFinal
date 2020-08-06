from django.shortcuts import render, redirect
from .forms import AccountForm
from .models import Account
from django.contrib.auth.models import User, auth
# Create your views here.
def account(request):
    account = Account.objects.get(id=request.user.id)
    context = {'account': account}
    return render(request, 'accounts/account.html', context)

def update(request):
    account = Account.objects.get(id=request.user.id)
    form = AccountForm(instance=account)
    if request.method == 'POST':
        form = AccountForm(request.POST, request.FILES)
        if forms.is_valid():
            forms.save()
    context = {'form': form}
    return render(request, 'accounts/update.html', context)
