from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

from django.utils.translation import gettext as _ 

class Cateogory(models.Model):
    category=models.CharField(max_length=250)
    def __str__(self):
        return self.category

class Bookinfo(models.Model):
    
   
    title = models.CharField(max_length=255)
    description = models.TextField()
    seller = models.ForeignKey(User, on_delete=models.CASCADE)
    original_price = models.DecimalField(max_digits=8, decimal_places=2)
    selling_price = models.DecimalField(max_digits=8, decimal_places=2)
    condition = models.CharField(max_length=255)
    category = models.ForeignKey(Cateogory, on_delete=models.CASCADE)
    image = models.ImageField( upload_to='books/images',max_length=None)
    latitude = models.FloatField(default=None)
    longitude = models.FloatField(default=None)
    location=models.CharField(max_length=200,default="Gharmi, Pokhara-16, Pokhara, Kaski")
    added_date = models.DateField(default=None)
    def __str__(self):
     return self.title
    


    
class Bookedmodel(models.Model):
   buyer_id=models.PositiveIntegerField()
   book_id=models.PositiveIntegerField()
   booked_request_date=models.DateField()
   booked_status=models.BooleanField(default=False)
   notification_status=models.BooleanField(default=None,null=True)