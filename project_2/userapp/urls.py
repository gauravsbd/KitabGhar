from . import views
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("login",views.login_form, name= "login"),
    path("signup",views.signup_form , name = "signup"),
    path("logout/",auth_views.LogoutView.as_view(),name = "logout"),
    ]