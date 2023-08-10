from django.shortcuts import render
from django.http import HttpResponse,HttpRequest
from .forms import searchform
from .models import searchmodel
from django.views import View
from bookinfo.models import Bookinfo
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
    
# Create your views here.
class book_form(View):
     
      def get(self, request,):
        title = request.GET.get('Title')
        category = request.GET.get('category')
        books=Bookinfo.objects.filter(category=category)
        matching_books = process.extractBests(title, [book.title for book in books], scorer=fuzz.ratio, )
        book_title = [match[0] for match in matching_books if match[1] >= 40]
        filter_books = books.filter(title__in=book_title).exclude(seller_id=request.user.id)
        context ={'search_books':filter_books}
        return render (request,"search_result.html",context)
        
      def post(self, request, *args, **kwargs):
          pass 