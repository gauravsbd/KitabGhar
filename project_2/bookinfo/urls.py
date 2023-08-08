from . import views
from django.contrib import admin
from django.urls import path



urlpatterns = [
    path("bookinfo/", views.book_form.as_view() , name='bookinfo'),
    path("editbook/",views.edit_books.as_view(),name="editbook"),
    path("mailsend/",views.send_mail,name='send_mail'),
] 
