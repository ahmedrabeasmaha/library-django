from django.shortcuts import render

# Create your views here.
from django.contrib.auth import login, authenticate, logout, get_user_model
from .forms import SignUpForm, LogInForm, AddBookForm, ChangePasswordForm, ChangePicForm
from django.shortcuts import redirect
from .models import Profile
from book.models import Book, BorrowedBook

def reg_log(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST' and request.POST.get('submit') == 'register':
            log_form = LogInForm()
            reg_form = SignUpForm(request.POST)
            if reg_form.is_valid():
                reg_form.save()
                username = reg_form.cleaned_data.get('username')
                password = reg_form.cleaned_data.get('password1')
                user = authenticate(username=username, password=password)
                login(request, user)
                return redirect('home')
        elif request.method == 'POST' and request.POST.get('submit') == 'login':
            reg_form = SignUpForm()
            log_form = LogInForm(data=request.POST)
            if log_form.is_valid():
                username = log_form.cleaned_data.get('username')
                password = log_form.cleaned_data.get('password')
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('home')
        else:
            reg_form = SignUpForm()
            log_form = LogInForm()
        context = {
            'reg_form':reg_form,
            'log_form':log_form,
        }
        return render(request, 'login.html', context)

def log_out(request):
    logout(request)
    return redirect('home')

def users(request):
    users = get_user_model().objects.filter(is_superuser=False)
    user = request.user
    pic = Profile.objects.get(user=user).pic
    if request.method == 'POST':
        users = get_user_model().objects.filter(is_superuser=False, id=request.POST['id'])
    context = {
        'users': users,
        'user': user,
        'pic': pic,
    }
    return render(request, 'users.html', context)

def all_books(request):
    books = Book.objects.all()
    user = request.user
    pic = Profile.objects.get(user=user).pic
    context = {
        'books': books,
        'user': user,
        'pic': pic,
    }
    return render(request, 'allbooks.html', context)

def borrowed_books(request):
    if request.user.is_staff:
        books = BorrowedBook.objects.select_related()
    else:
        books = BorrowedBook.objects.select_related()
        books = BorrowedBook.objects.filter(user=request.user.id)
    context = {
        'books': books,
    }
    return render(request, 'borrowedbooks.html', context)

def add_book(request):
    if request.method == 'POST':
        form = AddBookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        form = AddBookForm()
    else:
        form = AddBookForm()
        form.initial['user'] = request.user.id
    context = {
        'form': form,
    }
    return render(request, 'addbooks.html', context)

def change_password(request):
    if request.method == 'POST':
        form = ChangePasswordForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            logout(request)
            return redirect('home')
        form = ChangePasswordForm(user=request.user)
    else:
        form = ChangePasswordForm(user=request.user)
    context = {
        'form': form,
    }
    return render(request, 'changepassword.html', context)

def delete(request, id):
    book = Book.objects.get(id=id)
    book.delete()
    return redirect('all_books')

def edit(request, id):
    book = Book.objects.get(id=id)
    image = str(book.pic).split('/')
    if request.method == 'POST':
        form = AddBookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()
            return redirect('all_books')
        book = Book.objects.get(id=id)
        image = str(book.pic).split('/')
    else:
        form = AddBookForm(instance=book)
    context = {
        'form': form,
        'id' : id,
        'book': book,
        'image': image[1],
    }
    return render(request, 'addbooks.html', context)

def return_book(request, id):
    book = BorrowedBook.objects.get(id=id)
    book.delete()
    return redirect('borrowed_books')

def edit_profile(request):
    profile = Profile.objects.get(user=request.user.id)
    image = str(profile.pic).split('/')
    if request.method == 'POST':
        form = ChangePicForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('home')
        profile = Profile.objects.get(user=request.user.id)
        image = str(profile.pic).split('/')
    else:
        form = ChangePicForm(instance=profile)
    context = {
        'form': form,
        'profile': profile,
        'image': image[1],
    }
    return render(request, 'editprofile.html', context)