from bookinfo.models import Cateogory
from userapp.models import userinfomodel
from bookinfo.models import Bookedmodel,Bookinfo
from searchapp.models import searchmodel 
from django.contrib.sessions.models import Session
from django.contrib.messages import get_messages
from django.http import JsonResponse


#setting up the session value for the notification count 
def set_session(request):
        if request.user.is_authenticated:
            
            obj=searchmodel.objects.filter(user_id=request.user)
            obj=obj.exclude(notification_status=None)
            json_search_notification_data=[]
            notification_count=0
            for obj in obj:
                search_notification_data={
                "title":obj.Title,
                "category":obj.category.category,
                "book_id":obj.book_id,
                "notification_status":obj.notification_status
                }
                json_search_notification_data.append(search_notification_data)
                if obj.notification_status is None:
                   notification_count+=1
            # code for the activebooks pending notification
            json_pending_notification_data=[]
            obj=Bookedmodel.objects.all()
            for obj in obj:
                bookobj=Bookinfo.objects.get(id=obj.book_id)
                if(bookobj.seller==request.user):
                    if(obj.booked_status==False):
                        buyer=userinfomodel.objects.filter(user_id=obj.buyer_id)
                        for buyer in buyer:
                            pending_notification_data={
                                "buyer_name":buyer.Name,
                                "book_name":bookobj.title
                            }
                            if obj.notification_status is None:
                              notification_count+=1
                            json_pending_notification_data.append(pending_notification_data)   
            request.session["notification_count"]=notification_count
           


def global_context(request):
    set_session(request)
    # Add your global context data here
    category=Cateogory.objects.all()
    context={'category':category}
    if request.user.is_authenticated:
        id=request.user.id  
        userdata = userinfomodel.objects.filter(user_id=id)
        category = Cateogory.objects.all()
   #code for the notification context
        notification_count = request.session.get('notification_count', 0)
        context={'category':category,'userdata':userdata,'notification_count':notification_count}
    return context 
        

# def messages(request):
#     message_list = list(get_messages(request))
#     message_list_with_header=[]
#     for message in message_list:
#         message_list_with_header.append(
#             {
#                 "header":message.level_tag,
#                 "message":message.message
#             }
#         )
#     return JsonResponse({'messages': message_list_with_header})    
    