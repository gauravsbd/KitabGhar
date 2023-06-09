from django.shortcuts import render
from django.http import HttpResponse
from .forms import searchform
from .models import searchfield
# Create your views here.
def form_view(request):

     if request.method == 'POST':
         
         pass
     else:
          
         form = searchform()
         context = {"form":form}
         return render(request,"index.html",context)