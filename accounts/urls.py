from django.urls import path
from .views import UserLoginView,UserRegisterView,UserProfileView,UserLogoutView,ReturnBook

urlpatterns = [
    path('login/',UserLoginView.as_view(),name = 'login'),
    path('register/',UserRegisterView.as_view(),name = 'register'),
    path('profile/',UserProfileView,name = 'profile'),
    path('logout/',UserLogoutView.as_view(),name = 'logout'),
    path('return/<int:book_id>/',ReturnBook,name = 'return'),
]
