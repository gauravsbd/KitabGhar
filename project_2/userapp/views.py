from django.shortcuts import render
from django.contrib import messages
from .forms import signupform
from django.contrib.auth.models import User

 


from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate , login , logout 
<<<<<<< HEAD
from django.http import HttpResponseRedirect 

=======
from django.http import HttpResponseRedirect
from django.views import View
from .forms import userinfoform
from .models import userinfomodel
# from django.http import HttpResponse
# from .forms import loginform , signupform
# from .models import loginmodel
# # from .forms import signupform
# # Create your views here.
>>>>>>> 2e627352b06550f617ba7c4191e7517c95d33300
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
<<<<<<< HEAD
=======
            
        return HttpResponseRedirect("login")
        
>>>>>>> 2e627352b06550f617ba7c4191e7517c95d33300
        
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
<<<<<<< HEAD
    return render (request,'userapp/signup_form.html',{'signupform':fm})

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')
=======
    return render (request,'signup_form.html',{'signupform':fm})

class profile_view(View):
    def get(self, request, ):

        if request.user.is_authenticated:

          id=request.user.id
          email = request.user.email
          
          data = userinfomodel.objects.get(user_id=id)
          context={"userdata":data,"email":email}

          return render(request,"profile.html",context)
    

    def post(self, request, *args, **kwargs):
        return HttpResponse('POST request!')
class profileedit_view(View):
    def get(self, request, ):
        fm=userinfoform()
        return render(request,"profileedit.html",{'userform':fm})
    

    def post(self, request, *args, **kwargs):
        fm = userinfoform(request.POST,request.FILES)
        if fm.is_valid():
           
            fm.save()
            return HttpResponse('POST request!')
           
>>>>>>> 2e627352b06550f617ba7c4191e7517c95d33300

