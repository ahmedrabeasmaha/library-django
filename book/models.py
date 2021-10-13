from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Book(models.Model):
    name = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    pic = models.ImageField(default='books/book.png', upload_to='books/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class BorrowedBook(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.OneToOneField(Book, on_delete=models.CASCADE)
    return_date = models.DateField()

    def __str__(self):
        return str(self.book)

class FeaturedProduct(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.book)

class RecentReleases(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.book)
