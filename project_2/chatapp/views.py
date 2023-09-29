from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Chatmodel
from django.views import View
from django.db.models import Q
from django.http import JsonResponse

# Create your views here.
class chatView(View):
    def get(self,request):
       conversation=[]
       booked_id=request.GET.get("booked_id")
       chatConversation=Chatmodel.objects.filter(booked_id=booked_id).order_by("date_time")
       chatNotification=0
       for data in chatConversation:
           chat={
            "message":data.message,
            "sender_id":data.sender_id.id  
           }
           conversation.append(chat)
           if(data.view_status is None):
               chatNotification=chatNotification+1
       response={
           "conversation":conversation,
           "user_id":request.user.id,\
           "chatNotification":chatNotification
       }
       print(response)
       return JsonResponse(response)

    def post(self,request):
        print("done")
        print(request.POST.get("booked_id"))
        pass