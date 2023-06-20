from django.db import models
from django.contrib.auth.models import User

from django.utils.translation import gettext as _   
class Bookinfo(models.Model):
    category = (
        ('+2', '+2'),
        ('Me', 'Medical'),
        ('En', 'Engineering'),
        ('No', 'Novels & More'),
        ('Sc', 'School'),
    )
   
    title = models.CharField(max_length=255)
    description = models.TextField()
    seller = models.ForeignKey(User, on_delete=models.CASCADE)
    original_price = models.DecimalField(max_digits=8, decimal_places=2)
    selling_price = models.DecimalField(max_digits=8, decimal_places=2)
    condition = models.CharField(max_length=255)
    category = models.CharField(max_length=100,choices=category)
    image = models.ImageField( upload_to='books/images', height_field=None, width_field=None, max_length=None)
      # longitude = models.FloatField()
      # latitude = models.FloatField()
 
