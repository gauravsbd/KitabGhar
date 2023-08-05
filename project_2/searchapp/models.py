from django.db import models
from django import forms 
from django.contrib.auth.models import User
from bookinfo.models import Cateogory

class searchmodel(models.Model):
    Title=models.CharField(max_length=100)
    category=models.ForeignKey(Cateogory,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
        return(self.Title)