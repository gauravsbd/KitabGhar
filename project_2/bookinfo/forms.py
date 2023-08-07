from .models import Bookinfo
from django.forms import ModelForm
from django import forms
 

class Bookform(ModelForm):
    class Meta:
        model = Bookinfo
        exclude=['seller','added_date']
    
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class':'form-control'})
  
