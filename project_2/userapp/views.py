from django.shortcuts import render
from django.contrib import messages
from .forms import signupform
from django.contrib.auth.models import User
from bookinfo.models import Cateogory,Bookinfo,Bookedmodel
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate , login , logout 
from django.http import HttpResponseRedirect 
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect,HttpResponse
from django.views import View
from .forms import userinfoform
from .models import userinfomodel
from django.http import JsonResponse
from bookinfo.forms import editBookform
from django.core.files.storage import default_storage
from searchapp.models import searchmodel
from datetime import datetime
from bookinfo.models import Soldbookmodel

#  Create your views here.
def login_form(request):
    if request.method == 'POST':
        fm = AuthenticationForm(request=request, data=request.POST)
        if fm.is_valid():
            uname = fm.cleaned_data['username']
            upass = fm.cleaned_data['password']
            user= authenticate(username=uname,password=upass)
            if user is not None:
                login(request,user)
                messages.success(request,'Logged in succesfully')
                return HttpResponseRedirect("/")
                  
    else: 
          fm = AuthenticationForm()   

    context = {"loginform":fm}
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
    messages.info(request,"Log out succefully")
    return HttpResponseRedirect('/')

class profile_view(View):
    def get(self, request, ):
        if request.user.is_authenticated:
          email = request.user.email
          fm=userinfoform()
          bfm=editBookform(prefix='bookform')
          #code for the activebooks count
          activebooks=Bookinfo.objects.filter(seller=request.user.id)
          activebooks_count=activebooks.count()
          #code for the bookedbooks count
          bookedbooks=Bookedmodel.objects.filter(buyer_id=request.user.id)
          bookedbooks_count=bookedbooks.count()

          soldbookobj=Soldbookmodel.objects.filter(user_id=request.user.id)
          soldbookcount=0
          for soldbook in soldbookobj:
              soldbookcount=soldbookcount+1
          
          context={"email":email,"userform":fm,"bookform":bfm,"activebooks_count":activebooks_count,"bookedbooks_count":bookedbooks_count,"soldbooks_count":soldbookcount}
          return render(request,"profile.html",context)

          

    def post(self, request, *args, **kwargs):
        # fm = userinfoform(request.POST,request.FILES)
        # if fm.is_valid():
           
        #     fm.save()
        #     return HttpResponse('POST request!')
        pass
        
@csrf_exempt
def edit_profile(request):
        print("done")
        Name = request.POST['Name']
        Phone_Number =request.POST['Phone_Number']
        latitude=request.POST['latitude']
        address=request.POST['address']
        longitude=request.POST['longitude']
        try:  
            obj=userinfomodel.objects.get(user_id=request.user)
            obj.Name = Name
            obj.Phone_Number = Phone_Number
            obj.Address=address
            obj.latitude=latitude
            obj.longitude=longitude
            obj.save()
             
        except userinfomodel.DoesNotExist:
                user=User.objects.get(id=request.user.id)  
                obj=userinfomodel()
                obj.Name = Name
                obj.Phone_Number = Phone_Number
                obj.Address=address
                obj.latitude=latitude
                obj.longitude=longitude
                obj.user=request.user
                obj.Register_date=user.date_joined.date()
                obj.save()
                print("done")
        messages.success(request,'Profile edited successfully')
         
        data = {
                'data': 'done'
        }
        return JsonResponse(data,content_type="application/json",safe=False)

    
@csrf_exempt
def edit_profile_photo(request):
    if request.method == 'POST' and request.FILES.get('image'):
        image_file = request.FILES['image']
        user_id=request.user.id
        obj=userinfomodel.objects.get(user_id=user_id)
        if obj.Profile_photo:
            previous_photo_path = obj.Profile_photo.path
            if default_storage.exists(previous_photo_path):
                default_storage.delete(previous_photo_path)
        
        # Save the new photo file
        new_photo_path = f'user/images/{user_id}_{image_file.name}'
        default_storage.save(new_photo_path, image_file)
        
        # Update the Profile_photo field
        obj.Profile_photo.name = new_photo_path
        obj.save()
        messages.success(request,'Profile picture updated successfully ')
        image_url=obj.Profile_photo.url
        data={
            "image_url":image_url
        }
        return JsonResponse(data,content_type="application/json",safe=False)

class notification(View):
    # notification for the searchstatus
    def get(self,request):
        request.session["notification_count"]=0
        request.session.save()
        obj=searchmodel.objects.filter(user_id=request.user)
        obj=obj.exclude(notification_status=None)
        json_search_notification_data=[]
        for obj in obj:
            search_notification_data={
            "title":obj.Title,
            "category":obj.category.category,
            "book_id":obj.book_id,
            "notification_status":obj.notification_status,
            "search_id":obj.id
             }
            obj.notification_status=False
            obj.save()
            json_search_notification_data.append(search_notification_data)

        # code for the activebooks pending notification
        json_pending_notification_data=[]
        obj=Bookedmodel.objects.all()
        for obj in obj:
            bookobj=Bookinfo.objects.get(id=obj.book_id)
            if(bookobj.seller==request.user):
                if(obj.booked_status==False):
                  
                    buyer=userinfomodel.objects.get(user_id=obj.buyer_id)
                    pending_notification_data={
                         "buyer_name":buyer.Name,
                         "book_name":bookobj.title,
                         "pending_id":obj.id
                    }
                    obj.notification_status=False
                    obj.save()
                    json_pending_notification_data.append(pending_notification_data)   
        json_notification_data={"search_notification":json_search_notification_data,"pending_notification":json_pending_notification_data}
       
        return JsonResponse(json_notification_data,content_type="application/json",safe=False)
        