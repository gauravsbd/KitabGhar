from django.shortcuts import render
from django.contrib import messages
from .forms import signupform
from django.contrib.auth.models import User
from bookinfo.models import Cateogory,Bookinfo
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate , login , logout 
from django.http import HttpResponseRedirect 

from django.http import HttpResponseRedirect,HttpResponse
from django.views import View
from .forms import userinfoform
from .models import userinfomodel
from django.http import JsonResponse

# # Create your views here.
def login_form(request):
    if request.method == 'POST':
        fm = AuthenticationForm(request=request, data=request.POST)
        if fm.is_valid():
            uname = fm.cleaned_data['username']
            upass = fm.cleaned_data['password']
            user= authenticate(username=uname,password=upass)
            if user is not None:
             login(request,user)
             return HttpResponseRedirect("/")
        return HttpResponseRedirect("login")
    else:
         form = AuthenticationForm()
         context = {"loginform":form}
         return render(request,"userapp/login_form.html",context)

def signup_form(request):
    if request.method == "POST":
        fm = signupform(request.POST)
        if fm.is_valid():
            
            fm.save()
            messages.success(request,'Account Created successfully ')
    else:    
       fm = signupform()

    return render (request,'userapp/signup_form.html',{'signupform':fm})

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')


class profile_view(View):
    def get(self, request, ):
        if request.user.is_authenticated:
          email = request.user.email
          fm=userinfoform()
          activebooks=Bookinfo.objects.filter(seller_id=request.user.id)
          
          context={"email":email,"userform":fm,"activebooks":activebooks}
          return render(request,"profile.html",context)

          

    def post(self, request, *args, **kwargs):
        # fm = userinfoform(request.POST,request.FILES)
        # if fm.is_valid():
           
        #     fm.save()
        #     return HttpResponse('POST request!')
        pass
        
class edit_profile(View):
    def get(self,request):
        print("ok")
        user_id = request.GET['user_id']
        Name = request.GET['Name']
        Phone_Number =request.GET['Phone_Number']
        print("ok")
        image_file =request.FILES.get["Profile_photo"] 
        print("ok")
        print(image_file)
        try:  
           c=userinfomodel.objects.get(user_id=user_id)
           # import json
           # data = list(c.values())
           # json_data = json.dumps(data)
           c.Name = Name
           c.Phone_Number = Phone_Number
           if image_file:
               c.Profile_photo = image_file
           c.save()

        except userinfomodel.DoesNotExist:
            c=userinfomodel(Name=Name,Phone_Number=Phone_Number,)

        data = {
                'data': 'done'
        }
        return JsonResponse(data)

    def post(self, request, *args, **kwargs):
        pass