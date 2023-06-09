from django.shortcuts import render
from bookinfo.models import Bookinfo

# Create your views here.
from django.http import HttpResponse
# from .forms import searchform
# from .models import searchfield
# Create your views here.
def form_view(request):

    data = Bookinfo.objects.all()
    
    return render(request,"baseapp/home.html",{ "data" :data})
