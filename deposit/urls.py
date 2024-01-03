from django.urls import path
from .views import UserDeposit

urlpatterns = [
    path('',UserDeposit,name = 'deposit')
]
