# We need to create separate urls.py file for each app in myProject

from django.urls import path
from .views import index

urlpatterns = [
    path('', index, name="index"),
]