from django.shortcuts import render
from bookinfo.models import Bookinfo
from userapp.models import userinfomodel
from bookinfo.models import Cateogory
from searchapp.forms import searchform
from django.core.paginator import Paginator
from django.contrib.messages import get_messages
from django.http import JsonResponse


def form_view(request):
    categories = Cateogory.objects.all()[:3]
    filter_books = []

    for category in categories:
        books = Bookinfo.objects.filter(category=category)
        paginator = Paginator(books, 4)  # Display 4 books per page initially
        page_number = request.GET.get('page')
        books = paginator.get_page(page_number)
        filter_books.append({'category': category, 'books': books})

    form = searchform()
    context = {"filter_books": filter_books, "form": form}
    
    if request.user.is_authenticated:
        return render(request, "baseapp/home.html", context)
    else:
        return render(request, "baseapp/home.html", context)

def about_us(request):
    if request.user.is_authenticated:
       
        return render(request,"baseapp/about_us.html",)
    
def messages(request):
    
    message_list = list(get_messages(request))
    message_list_with_header=[]
    for message in message_list:
        message_list_with_header.append(
            {
                "header":message.level_tag,
                "message":message.message
            }
        )
       
    return JsonResponse({'messages': message_list_with_header})    
    