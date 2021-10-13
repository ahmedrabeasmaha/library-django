from django.contrib import admin

# Register your models here.
from .models import Category, Book, BorrowedBook, FeaturedProduct, RecentReleases

admin.site.register(Category)
admin.site.register(Book)
admin.site.register(BorrowedBook)
admin.site.register(FeaturedProduct)
admin.site.register(RecentReleases)