# mynewapp/views.py
from django.shortcuts import render

def new_page(request):
    return render(request, 'mynewapp/new_page.html')
