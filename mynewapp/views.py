# mynewapp/views.py
from django.shortcuts import render, redirect
from .models import Book
from .forms import BookForm

def new_page(request):
    return render(request, 'mynewapp/new_page.html')


def books_index(request):
    books = Book.objects.all()
    return render(request, 'mynewapp/books_index.html', {'books': books})

def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('books_index')
    else:
        form = BookForm()
    return render(request, 'mynewapp/add_book.html', {'form': form})