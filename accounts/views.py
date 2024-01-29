from django.shortcuts import render,redirect
from django.contrib.auth.views import LoginView,LogoutView
from django.views.generic import FormView,TemplateView
from .forms import RegisterUserForm
from django.urls import reverse_lazy
from django.contrib.auth import login, logout
from .models import UserProfile
from books.models import Borrowed
from django.contrib import messages

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
        messages.success(self.request, 'Logout successfully')
        return reverse_lazy('home')
# class UserLogoutView(LogoutView):
#     def get_success_url(self):
#         if self.request.user.is_authenticated:
#             logout(self.request)
#         return reverse_lazy('home')
     
        
class UserProfileView1(TemplateView):
    template_name = 'accounts/profile.html'

def UserProfileView(request):
    # profile = UserProfile.objects.get(user=request.user.id)
    # totalAmount = profile.account_balance
    borrowed  = []
    try:
        profile = UserProfile.objects.get(user=request.user)
        totalAmount = profile.account_balance
        borrowed1 = Borrowed.objects.filter(user = profile.user)
        borrowed = borrowed1

    except:
        totalAmount = None
    return render(request, 'accounts/profile.html', {'totalAmount': totalAmount,'borrowed':borrowed})

def ReturnBook(request,book_id):
    borrowed = Borrowed.objects.get(id = book_id)
    user = UserProfile.objects.get(id = request.user.id)
    
    user.account_balance = user.account_balance + borrowed.book.price
    user.save()

    return redirect('profile')