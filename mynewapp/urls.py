# mynewapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('newpage/', views.new_page, name='new_page'),
    path('books/', views.books_index, name='books_index'),
    path('books/add/', views.add_book, name='add_book'),
]
