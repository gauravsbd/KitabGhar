from django.shortcuts import render
from .forms import Bookform
from .models import Bookinfo
from django.http import HttpResponse
from django.views import View
from userapp.models import userinfomodel
from bookinfo.models import Cateogory

class book_form(View):
    def get(self, request, ):
         form = Bookform()
         context = {"bookform":form,}
         return render(request,"book_form.html",context)
    
    
    def post(self, request, *args, **kwargs):
      
       fm = Bookform(request.POST, request.FILES)
       if fm.is_valid():
        fm.save()  
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
       