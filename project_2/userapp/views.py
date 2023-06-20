from django.shortcuts import render
from django.contrib import messages
from .forms import signupform
from django.http import HttpResponse


from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate , login , logout 
from django.http import HttpResponseRedirect
from django.views import View
from .forms import userinfoform
from .models import userinfomodel
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
            
        return HttpResponseRedirect("login")
        
        
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
            
            fm.save()
            messages.success(request,'Account Created successfully ')
    else:    
       fm = signupform()
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
           

