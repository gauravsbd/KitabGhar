from django.shortcuts import render
from .forms import Bookform
from .models import Bookinfo
from django.http import HttpResponse,JsonResponse
from django.views import View
from userapp.models import userinfomodel
from .models import Cateogory,Bookinfo
from datetime import date
import json
from django.forms.models import model_to_dict

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
       