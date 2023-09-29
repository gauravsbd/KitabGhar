from . import views
from bookinfo.views import booked_books,cancel_book
from userapp.views import notification
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
    path("edit-profile/",views.edit_profile),
    path("booked-book/",booked_books.as_view()),
    path("cancel-book/",cancel_book.as_view()),
    path("notification/",notification.as_view()),
    path("edit-profile-photo/",views.edit_profile_photo)
    ]