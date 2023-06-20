from . import views
from django.contrib import admin
from django.urls import path
from bookinfo.views import book_detail

urlpatterns = [
    path("",views.form_view, name= "home"),
    path("book-detail/<int:id>", book_detail.as_view(), name="book_detail"),
    path("aboutus" ,views.about_us, name="aboutus")
   
    
]
