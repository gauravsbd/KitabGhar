
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from django import forms
from .models import userinfomodel
from django.forms import ModelForm


class signupform(UserCreationForm):
	password1 = forms.CharField(label='password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
	password2 = forms.CharField(label='Confirm password (again)', widget=forms.PasswordInput(attrs={'class':'form-control'}))
	class Meta:	
		model = User
		 
		fields = [ 'username','first_name','last_name','email',]
		labels ={'email':"Email"}

	def __init__(self,*args,**kwargs):
			super().__init__(*args,**kwargs)
			for field in self.fields.values():
				field.widget.attrs.update({'class':'form-control'})
 
class userinfoform(ModelForm):
	class Meta:
		model = userinfomodel	
		fields='__all__'

	def __init__(self,*args,**kwargs):
			super().__init__(*args,**kwargs)
			for field in self.fields.values():
				field.widget.attrs.update({'class':'form-control'})
		 	