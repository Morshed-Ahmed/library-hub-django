from django.shortcuts import render,redirect
from .forms import DepositForm
from accounts.models import UserProfile
from django.contrib import messages
from django.core.mail import send_mail,EmailMultiAlternatives
from django.template.loader import render_to_string

# Create your views here.
def UserDeposit(request):
    profile = UserProfile.objects.get(user=request.user.id)
    totalAmount = profile.account_balance
    if request.method == 'POST':
        form = DepositForm(request.POST )
        if form.is_valid():
            amount = form.cleaned_data['amount']
            if amount <= 0:
                return redirect('deposit')  

            profile = UserProfile.objects.get(user=request.user.id)
            profile.account_balance += amount
            profile.save()  
            messages.success(request,'Deposit successful') 
            email_subject = "Successful Deposit Confirmation"
            email_body = render_to_string(
                'deposit_email.html',
                {'amount': amount}
            )
            email = EmailMultiAlternatives(
                subject=email_subject, body=email_body, to=[request.user.email]
            )
            email.attach_alternative(email_body, 'text/html')
            email.send()
            messages.success(request, ' Please check deposit confirmation email.')
            return redirect('deposit')
    else:
        form = DepositForm()
    return render(request, 'deposit.html', {'form': form,'totalAmount': totalAmount})

def UserProfileView(request):
    user_profile = UserProfile.objects.get(user=request.user.id)
    user_deposit = user_profile.account_balance
    return render(request, 'deposit.html', {'user_deposit': user_deposit})