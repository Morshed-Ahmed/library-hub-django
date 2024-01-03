from django.urls import path
from .views import HomeView,book_details,Borrowed_book

urlpatterns = [
    path('',HomeView,name = 'home'),
    path('category/<str:category_name>/',HomeView, name = 'category_wise_books'),
    path('book/<int:book_id>/',book_details, name = 'book_details'),
    path('borrowed_book/<int:book_id>/',Borrowed_book, name = 'borrowed_book'),
]