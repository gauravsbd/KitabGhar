from django.shortcuts import render
from .forms import Bookform
from .models import Bookinfo
from django.http import HttpResponse,JsonResponse
from django.views import View
from userapp.models import userinfomodel
from .models import Cateogory,Bookinfo,Bookedmodel
from datetime import date
from django.contrib.auth.models import User
import json
from django.forms.models import model_to_dict
import datetime
 

class book_form(View):
    def get(self, request, ):
         form = Bookform()
         context = {"bookform":form,}
         return render(request,"book_form.html",context)
    
    
    def post(self, request, *args, **kwargs):
      
       fm = Bookform(request.POST, request.FILES)
       if fm.is_valid():
        bk= Bookinfo()
        title = fm.cleaned_data['title']
        description = fm.cleaned_data['description']
        original_price = fm.cleaned_data['original_price']
        selling_price = fm.cleaned_data['selling_price']
        condition = fm.cleaned_data['condition']
        category = fm.cleaned_data['category']
        latitude= fm.cleaned_data['latitude']
        longitude= fm.cleaned_data['longitude']
        added_date=date.today()
        image=fm.cleaned_data['image']
        seller=request.user
        bk.title=title
        bk.description=description
        bk.original_price=original_price
        bk.selling_price=selling_price
        bk.condition=condition
        bk.category=category
        bk.latitude=latitude
        bk.longitude=longitude
        bk.added_date=added_date
        bk.image=image
        bk.seller=seller
        bk.save()  
        return HttpResponse("Done")  


class book_detail(View):
    def get(self, request, id):
         
          data = Bookinfo.objects.get(id=id)
          user_id = data.seller
          seller = userinfomodel.objects.filter(user_id=user_id)
          
          context={"data":data,"seller":seller,}
          return render(request,"book_detail.html",context)
    

    def post(self, request, *args, **kwargs):
        return HttpResponse('POST request!')
    
class all_books(View):
    def get(self, request, category):
       category_id = Cateogory.objects.values_list('id', flat=True).filter(category=category).first()
       data=Bookinfo.objects.filter(category=category_id)
       context={"data":data,}
       return render(request,"all_books.html",context)
    

    def post(self, request, *args, **kwargs):
        return HttpResponse('POST request!')
class edit_books(View):
    def get(self,request):
        try:
         id=request.GET['book_id']
         data=Bookinfo.objects.get(id=id)
         json_data={
             "title":data.title,
             "description":data.description,
             "original_price":data.original_price,
             "selling_price":data.selling_price,
             "condition":data.condition,
             "latitude":data.latitude,
             "longitude":data.longitude
         }
         if data.image:
             json_data['image_url'] = data.image.url
        except Bookinfo.DoesNotExist:
         return JsonResponse({'error': 'Book not found'}, status=404)     
           
        return JsonResponse(json_data)
    def post(self, request, *args, **kwargs):
        return HttpResponse('POST request!')    
       

# code to book book
class book_book(View):
    def get(self,request):

        if  request.user.is_authenticated:
            book_id=request.GET["book_id"]
            date=datetime.date.today()
            obj=Bookedmodel()
            obj.buyer_id=request.user.id
            obj.book_id=book_id
            obj.booked_request_date=date
            obj.save()
            return JsonResponse({'data':'done'})
        else:
            
            return JsonResponse({'error': 'authentication_required', 'redirect_url': '/login/'}, status=401)

   

class activebooks(View):
    def get (self,request):
        activebooks_queryset = Bookinfo.objects.filter(seller_id=request.user.id)
 
        booked_book_id=Bookedmodel.objects.values("book_id")
        id_list = [item['book_id'] for item in booked_book_id]
       
        modified_activebooks = []

        for book in activebooks_queryset:
    # Create a dictionary with the original attributes and the extra attribute
            id=book.id
            if id in id_list:
             
                book_book=Bookedmodel.objects.get(book_id=id)
                modified_book = {
                        'id':id,
                       'title': book.title,
                       'image':book.image.url,
                       'status':book_book.booked_status
                                  }
            else:
                modified_book = {
                        'id':id,
                       'title': book.title,
                       'image':book.image.url,
                                  }
            modified_activebooks.append(modified_book)
        return JsonResponse(modified_activebooks, content_type='application/json', safe=False)

    
class Pending_books(View):
    def get(self,request):
        id=request.GET["book_id"]
        obj=Bookedmodel.objects.get(book_id=id)
        obj.booked_status=True
        obj.save()
        data={
            "data":"done"
        }
        return JsonResponse(data,content_type='application/json',safe=False) 

class Restore_books(View):
    def get(self,request):
        id=request.GET["book_id"]
        obj=Bookedmodel.objects.get(book_id=id)
        obj.delete()
        data={
            "data":"done"
        } 
        return JsonResponse(data,content_type='application/json',safe=False)   

class profile_data(View):
    def get(self,request):

        activebooks_queryset = Bookinfo.objects.filter(seller_id=request.user.id)
 
        booked_book_id=Bookedmodel.objects.values("book_id")
        id_list = [item['book_id'] for item in booked_book_id]
       
        modified_activebooks = []

        for book in activebooks_queryset:
    # Create a dictionary with the original attributes and the extra attribute
            id=book.id
            if id in id_list:
             
                book_book=Bookedmodel.objects.get(book_id=id)
                modified_book = {
                        'id':id,
                       'title': book.title,
                       'image':book.image.url,
                       'status':book_book.booked_status
                                  }
            else:
                modified_book = {
                        'id':id,
                       'title': book.title,
                       'image':book.image.url,
                                  }
            modified_activebooks.append(modified_book)
        activebooks_count=len(modified_activebooks)
        return JsonResponse({"activebooks":activebooks_count},content_type="application/json",safe=False)      
       
class booked_books(View):
    def get(self,request):
        obj=Bookedmodel.objects.filter(buyer_id=request.user.id).values("book_id")
        id_list=[list["book_id"] for list in obj]
        for id in id_list:
          obj=Bookinfo.objects.get(id=id)
          print(obj)

        return JsonResponse({"data":"done"},content_type="application/json",safe=False)      
       
