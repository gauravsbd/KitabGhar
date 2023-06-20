from .models import Bookinfo
from django.forms import ModelForm
from django import forms

class Bookform(ModelForm):
    class Meta:
        model = Bookinfo
        fields =['title','description','seller','original_price','selling_price','condition','category','image','latitude','longitude','added_date']
