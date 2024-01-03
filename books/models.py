from django.db import models
from categories.models import Category
from django.contrib.auth.models import User

# Create your models here.
class Book(models.Model):
    image = models.ImageField(upload_to='books/media/uploads',blank = True, null = True)
    title = models.CharField(max_length=30,unique=True)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE,blank = True, null = True)
    author = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2,blank = True, null = True)

    def __str__(self):
        return self.title

class Borrowed(models.Model):
    book = models.ForeignKey(Book,on_delete= models.CASCADE)
    user = models.ForeignKey(User,on_delete= models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    return_date = models.DateTimeField(blank = True, null = True)

    def __str__(self):
        return f"{self.user}"


class Review(models.Model):
    book = models.ForeignKey(Book,on_delete= models.CASCADE)
    user = models.ForeignKey(User,on_delete= models.CASCADE)
    review = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comments by {self.user}"

