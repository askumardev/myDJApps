# We need to create separate urls.py file for each app in myProject

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
]