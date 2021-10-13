from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.reg_log, name='login_user'),
    path('logout/', views.log_out, name='logout_user'),
    path('users/', views.users, name='users'),
    path('all-books/', views.all_books, name='all_books'),
    path('borrowed-books/', views.borrowed_books, name='borrowed_books'),
    path('add-new-book/', views.add_book, name='add_book'),
    path('change-password/', views.change_password, name='password'),
    path('edit-profile/', views.edit_profile, name='edit_profile'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('edit/<int:id>/', views.edit, name='edit'),
    path('return-book/<int:id>/', views.return_book, name='return_book'),
    
]