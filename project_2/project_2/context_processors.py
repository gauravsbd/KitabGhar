from bookinfo.models import Cateogory
from userapp.models import userinfomodel

def global_context(request):
    # Add your global context data here
    category=Cateogory.objects.all()
    context={'category':category}
    if request.user.is_authenticated:
        id=request.user.id  
        userdata = userinfomodel.objects.filter(user_id=id)
        category = Cateogory.objects.all()
        context={'category':category,'user1':userdata}
    return context 
        
        
    