from django.shortcuts import render
from django.contrib import messages
from .forms import signupform
from django.http import HttpResponse

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate , login , logout 
from django.http import HttpResponseRedirect
# from django.http import HttpResponse
# from .forms import loginform , signupform
# from .models import loginmodel
# # from .forms import signupform
# # Create your views here.
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
         return render(request,"login_form.html",context)
    
# def signupform_view(request):

#     # return HttpResponse("hello")
#     if request.method == 'POST':
#          return HttpResponse("Done")
         
#          pass
#     else:
          
#          form = signupform()
#          context = {"signupform":form}
#          return render(request,"signup_form.html",context)    
# from django.contrib.auth.forms import UserCreationForm

def signup_form(request):
    if request.method == "POST":
        fm = signupform(request.POST)
        if fm.is_valid():
            messages.success(request,'Account Created successfully ')
            fm.save()
    else:    
       fm = signupform()
    return render (request,'signup_form.html',{'signupform':fm})
