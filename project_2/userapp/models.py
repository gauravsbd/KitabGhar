from django.db import models
from django.contrib.auth.models import User
 

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
    Address = models.CharField(max_length=20)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Profile_photo = models.ImageField(upload_to=("user/images"),max_length=None)
    latitude = models.FloatField()
    longitude = models.FloatField()
    Register_date = models.DateField()
    
   
    
   
   