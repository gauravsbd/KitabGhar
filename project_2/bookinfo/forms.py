from .models import Bookinfo
from django.forms import ModelForm
from django import forms
 

class Bookform(ModelForm):
    class Meta:
        model = Bookinfo
<<<<<<< HEAD
        fields =['title','description','seller','original_price','selling_price','condition','category','image']
       
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['title'].widget.attrs.update({'class':'form-control'})
        self.fields['description'].widget.attrs.update({'class':'form-control'})
        self.fields['seller'].widget.attrs.update({'class':'form-control'})
        self.fields['original_price'].widget.attrs.update({'class':'form-control'})
        self.fields['selling_price'].widget.attrs.update({'class':'form-control'})
        self.fields['condition'].widget.attrs.update({'class':'form-control'})
        self.fields['category'].widget.attrs.update({'class':'form-control'})
        self.fields['image'].widget.attrs.update({'class':'form-control'})
        
        
=======
        fields =['title','description','seller','original_price','selling_price','condition','category','image','latitude','longitude','added_date']
>>>>>>> 2e627352b06550f617ba7c4191e7517c95d33300
