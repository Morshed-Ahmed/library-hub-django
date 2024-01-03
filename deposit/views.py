from django.shortcuts import render,redirect
from .forms import DepositForm
from accounts.models import UserProfile
from django.contrib import messages

# Create your views here.
def UserDeposit(request):
    profile = UserProfile.objects.get(user=request.user)
    totalAmount = profile.account_balance
    if request.method == 'POST':
        form = DepositForm(request.POST )
        if form.is_valid():
            amount = form.cleaned_data['amount']
            if amount <= 0:
                return redirect('deposit')

            profile = UserProfile.objects.get(user=request.user)
            profile.account_balance += amount
            profile.save()  
            messages.success(request,'Deposit successful')    
            return redirect('deposit')
    else:
        form = DepositForm()
    return render(request, 'deposit.html', {'form': form,'totalAmount': totalAmount})

def UserProfileView(request):
    user_profile = UserProfile.objects.get(user=request.user)
    user_deposit = user_profile.account_balance
    return render(request, 'deposit.html', {'user_deposit': user_deposit})