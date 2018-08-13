from django.urls import path
from . import views

# start with blog
urlpatterns = [
    path('add_book/', views.add_book, name='add_book'),
	path('show_books/', views.show_books, name='show_books'),
]