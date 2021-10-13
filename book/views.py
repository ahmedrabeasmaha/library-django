from django.shortcuts import render

# Create your views here.
from user.models import Profile
from .models import Category, FeaturedProduct, RecentReleases, Book, BorrowedBook
from .forms import BorrowForm

def base_page(request):
    context = {}
    if request.user.is_authenticated:
        base_user = request.user
        pic = Profile.objects.get(user=request.user.id).pic
        main_category = Category.objects.all()
        context = {
            'base_user': base_user,
            'pic': pic,
            'main_category': main_category,
        }
        return context
    return context

def home(request):
    featured_products = FeaturedProduct.objects.select_related()
    recent_releases = RecentReleases.objects.select_related()
    # ids = []
    # for featured_product in featured_products:
    #     ids.append(featured_product.book.id)
    # featured_products = Book.objects.filter(id__in=ids)
    # ids = []
    # for recent_release in recent_releases:
    #     ids.append(recent_release.book.id)
    # recent_releases = Book.objects.filter(id__in=ids)
    context = {
        "featured_products": featured_products,
        "recent_releases": recent_releases,
    }
    return render(request, 'home.html', context)

def most_relases(request):
    books = RecentReleases.objects.all()
    ids = []
    for recent_release in books:
        ids.append(recent_release.book.id)
    books = Book.objects.filter(id__in=ids)
    context = {
        'books': books,
        'category': 'most recent releases',
    }
    return render(request, 'books.html', context)

def book(request, id):
    book = Book.objects.get(id=id)
    borrow = BorrowedBook.objects.filter(book=id)
    if request.method == 'POST':
        form = BorrowForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = BorrowForm()
        form.initial['user'] = request.user.id
        form.initial['book'] = book.id
    context = {
        'book': book,
        'form': form,
        'borrow': borrow,
    }
    return render(request, 'book.html', context)

def category(request, id):
    cat = Category.objects.get(id=id)
    books = Book.objects.filter(category=cat.id)
    context = {
        'books': books,
        'category': cat.name,
    }
    return render(request, 'books.html', context)
