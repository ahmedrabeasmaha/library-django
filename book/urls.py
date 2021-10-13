from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('most-recent-releases', views.most_relases, name='most_relases'),
    path('book/<int:id>', views.book, name='book'),
    path('category/<int:id>', views.category, name='category'),
]