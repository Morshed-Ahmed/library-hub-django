from django.shortcuts import render
from django.contrib.auth.views import LoginView,LogoutView
from django.views.generic import FormView,TemplateView
from .forms import RegisterUserForm
from django.urls import reverse_lazy
from django.contrib.auth import login, logout
from .models import UserProfile
from books.models import Borrowed

# Create your views here.
class UserLoginView(LoginView):
    template_name = 'accounts/login.html'
    def get_success_url(self):
        return reverse_lazy('home')

class UserRegisterView(FormView):
    template_name = 'accounts/register.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('profile')
    
    def form_valid(self,form):
        user = form.save()
        UserProfile.objects.create(user=user)
        login(self.request, user)
        return super().form_valid(form) 


class UserLogoutView(LogoutView):
    def get_success_url(self):
        if self.request.user.is_authenticated:
            logout(self.request)
        return reverse_lazy('home')
     
        
class UserProfileView1(TemplateView):
    template_name = 'accounts/profile.html'

def UserProfileView(request):
    profile = UserProfile.objects.get(user=request.user)
    totalAmount = profile.account_balance
    borrowed = Borrowed.objects.filter(user = profile.user)
    return render(request, 'accounts/profile.html', {'totalAmount': totalAmount,'borrowed':borrowed})