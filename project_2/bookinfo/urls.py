from . import views
from django.contrib import admin
from django.urls import path



urlpatterns = [
    path("bookinfo/", views.book_form.as_view() , name='bookinfo'),
] 
