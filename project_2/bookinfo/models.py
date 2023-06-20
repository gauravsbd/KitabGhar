from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

from django.utils.translation import gettext as _ 


# Create your models here.
# class Category(models.Model):
    # category = (
    #     ('', '+2'),
    #     ('', 'Medical'),
    #     ('', 'Engineering'),
    #     ('', 'Novels & More'),
    #     ('', 'School'),
    # )

#     name=models.CharField(max_length=100,choices=category)

   
class Bookinfo(models.Model):
    category = (
        ('+2', '+2'),
        ('Medical', 'Medical'),
        ('Engineering', 'Engineering'),
        ('Noovels & More', 'Novels & More'),
        ('School', 'School'),
    )
   
    title = models.CharField(max_length=255)
    description = models.TextField()
    seller = models.ForeignKey(User, on_delete=models.CASCADE)
    original_price = models.DecimalField(max_digits=8, decimal_places=2)
    selling_price = models.DecimalField(max_digits=8, decimal_places=2)
    condition = models.CharField(max_length=255)
    category = models.CharField(max_length=100,choices=category)
    image = models.ImageField( upload_to='books/images', height_field=None, width_field=None, max_length=None)
    latitude = models.FloatField(default=28.26689)
    longitude = models.FloatField(default=83.96851)
    added_date = models.DateField(default="2023-12-13")
