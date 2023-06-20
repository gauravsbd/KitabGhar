from django.shortcuts import render
from django.contrib import messages
from .forms import signupform
from django.contrib.auth.models import User

 

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate , login , logout 
from django.http import HttpResponseRedirect 

def login_form(request):

    # return HttpResponse("hello")
    if request.method == 'POST':
        fm = AuthenticationForm(request=request, data=request.POST)
        if fm.is_valid():
            uname = fm.cleaned_data['username']
            upass = fm.cleaned_data['password']
            user= authenticate(username=uname,password=upass)
            if user is not None:
             login(request,user)
             return HttpResponseRedirect("/")
        
    else:
         form = AuthenticationForm()
         context = {"loginform":form}
         return render(request,"userapp/login_form.html",context)
    

 

def signup_form(request):
    if request.method == "POST":
        fm = signupform(request.POST)
        if fm.is_valid():
            messages.success(request,'Account Created successfully ')
            fm.save()
    else:    
       fm = signupform()
    return render (request,'userapp/signup_form.html',{'signupform':fm})

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')

