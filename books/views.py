from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from django.views import View
from .models import  Book,Borrowed,Review
from categories.models import Category
from accounts.models import UserProfile
from django.contrib import messages
from .forms import ReviewForm

# Create your views here.
def HomeView(request,category_name = None):
    profile = UserProfile.objects.get(user=request.user.id)
    totalAmount = profile.account_balance
    data = Book.objects.all()
    brands = Category.objects.all()
    if category_name == 'all':
        data = Book.objects.all()
    elif category_name is not None:
        bt = Category.objects.get(name = category_name)
        print(data)
        data = Book.objects.filter(category = bt)
        print(data)
    return render(request,'books.html',{'data':data,'brands':brands,'totalAmount':totalAmount})


def book_details(request,book_id):
    profile = UserProfile.objects.get(user=request.user)
    totalAmount = profile.account_balance
    data = Book.objects.get(id = book_id)
    review = Review.objects.filter(book = book_id)

    is_borrow = bool
    borrow = Borrowed.objects.filter(user= profile.user,book= data)
    if len(borrow) > 0:
        is_borrow = True
    else:
        is_borrow = False

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.book = data
            review.save()
            return redirect('book_details', book_id=book_id)
    else:
        form = ReviewForm()
    return render(request,'book_details.html',{'data':data,'totalAmount':totalAmount,'form':form, 'review':review,'is_borrow':is_borrow})


def Borrowed_book(request,book_id):
    profile = UserProfile.objects.get(user=request.user)
    totalAmount = profile.account_balance
    data = Book.objects.get(id = book_id)
    if profile.account_balance >= data.price:
        profile.account_balance -= data.price
        profile.save()

        new_borrowed = Borrowed()
        new_borrowed.book = data
        new_borrowed.user = request.user
        new_borrowed.save()
        messages.success(request,'Borrowed book success')
    else:
        messages.success(request,'Your account is low')
    return redirect('book_details',data.id)

