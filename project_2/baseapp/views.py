from django.shortcuts import render
from bookinfo.models import Bookinfo
from userapp.models import userinfomodel

# Create your views here.
from django.http import HttpResponse
# from .forms import searchform
# from .models import searchfield
# Create your views here.
def form_view(request):

    data = Bookinfo.objects.all()
    id = request.user.id
    userdata = userinfomodel.objects.get(user_id=id)
    context ={"data":data,"userdata":userdata}
    return render(request,"baseapp/home.html",context)
def about_us(request):
    return render(request,"baseapp/about_us.html")