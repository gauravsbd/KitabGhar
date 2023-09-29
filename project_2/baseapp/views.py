from django.shortcuts import render
from bookinfo.models import Bookinfo
from userapp.models import userinfomodel
from bookinfo.models import Cateogory
from searchapp.forms import searchform


# Create your views here.
from django.http import HttpResponse

# Create your views here.
def form_view(request):
    filter_category=Cateogory.objects.filter()[:3]
    filter_books =[]
    for filter_category in filter_category:
            category_id = Cateogory.objects.values_list('id', flat=True).filter(category=filter_category).first()
            books=Bookinfo.objects.filter(category_id=category_id)
            filter_books.append(books)
    form=searchform()  
    context={"filter_books":filter_books,"form":form}
    if request.user.is_authenticated: 
        filter_category=Cateogory.objects.filter()[:3]
        filter_books =[]
        for filter_category in filter_category:
            category_id = Cateogory.objects.values_list('id', flat=True).filter(category=filter_category).first()
            books=Bookinfo.objects.filter(category_id=category_id).exclude(seller_id=request.user.id)
            filter_books.append(books)
        form=searchform()   
        context ={"filter_category":filter_category,"filter_books":filter_books,"form":form}
    return render(request,"baseapp/home.html",context)

def about_us(request):
    if request.user.is_authenticated:
       
        return render(request,"baseapp/about_us.html",)