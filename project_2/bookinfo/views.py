from django.shortcuts import render
from .forms import Bookform
from .models import Bookinfo
from django.http import HttpResponse
from django.views import View
def book_form(request):
    
    if request.method == 'POST':
      #  title = request.POST.get('title')
      #  description = request.POST.get('description')
      #  seller = request.user
      #  original_price = request.POST.get('original_price')
      #  selling_price = request.POST.get('selling_price')
      #  condition = request.POST.get('condition')
      #  category = request.POST.get('category')
      #  image = request.POST.get('image')
      #  fm= Bookinfo(title = title, description = description ,seller = seller , original_price = original_price , selling_price = selling_price, condition = condition ,category = category,image = image)
       fm = Bookform(request.POST, request.FILES)
       if fm.is_valid():
        fm.save()  
        return HttpResponse("Done")  
    else:
          
         form = Bookform()
         context = {"bookform":form}
         return render(request,"book_form.html",context)
    
class book_detail(View):
    def get(self, request, id):
          data = Bookinfo.objects.get(id=id)
          context={"data":data}
          return render(request,"book_view.html",context)
    

    def post(self, request, *args, **kwargs):
        return HttpResponse('POST request!')
    
   