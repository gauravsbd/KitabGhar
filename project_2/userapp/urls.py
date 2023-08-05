from . import views
 
from django.urls import path
from django.contrib.auth import views as auth_views
 


urlpatterns = [
    path("login/",views.login_form, name= "login"),
    path("signup/",views.signup_form , name = "signup"),
    path("logout/",views.user_logout,name = "logout"),
    path("forget_password/",auth_views.PasswordResetView.as_view(),name='password_reset'),
    path("forget_password_sent/",auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
    path("reset/<uidb64>/<token>/",auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path("forget_password_complete/",auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),
    path("logout/",auth_views.LogoutView.as_view(),name = "logout"),
    path("profile/",views.profile_view.as_view(),name = "profile"),
    path("editprofile/",views.edit_profile.as_view())
   

    ]