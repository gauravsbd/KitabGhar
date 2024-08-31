from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Chatmodel
from django.views import View
from django.db.models import Q
from django.http import JsonResponse
from datetime import datetime
from bookinfo.models import Bookedmodel

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
            "sender_id":data.sender_id
           }
           conversation.append(chat)
           if(data.view_status is None):
               chatNotification=chatNotification+1
       response={
           "conversation":conversation,
           "user_id":request.user.id,
           "chatNotification":chatNotification
       }
       print(response)
       return JsonResponse(response)

    def post(self,request):
        booked_id=request.POST.get("booked_id")
        bookobj=Bookedmodel.objects.get(id=booked_id)
        message=request.POST.get("message")
        obj=Chatmodel()
        obj.booked_id=bookobj
        obj.message=message
        obj.sender_id=request.user
        obj.date_time=datetime.now()
        obj.view_status=None
        obj.save()
        print("done")
        return JsonResponse({"data":"done"})