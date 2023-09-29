from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_delete
from django.dispatch import receiver
import os

# class signupmodel(models.Model):
    
    
#     Name = models.CharField(max_length=200,)
#     Contact_No = models.CharField(max_length=200,)
#     Email = models.EmailField(max_length=200,)
#     Password = models.CharField(max_length=20,)
# def __str__(self):
# 		return self.first_name + ' ' + self.last_name 
   
class userinfomodel(models.Model):
    Name = models.CharField(max_length=50)
    Phone_Number = models.CharField(max_length=10)
    Address = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Profile_photo = models.ImageField(upload_to=("user/images"),max_length=None)
    latitude = models.FloatField()
    longitude = models.FloatField()
    Register_date = models.DateField()

    
@receiver(pre_delete,sender=userinfomodel)
def delete_user_photo(sender,instance,**kwargs): 
    if instance.Profile_photo:
        if os.path.isfile(instance.Profile_photo.path):
            os.remove(instance.Profile_photo.path)

    
   
   