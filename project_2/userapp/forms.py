
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from django import forms

class signupform(UserCreationForm):
	password1 = forms.CharField(label='password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
	password2 = forms.CharField(label='Confirm password (again)', widget=forms.PasswordInput(attrs={'class':'form-control'}))
	class Meta:	
		model = User
		fields = [ 'username','first_name','last_name','email',]
		labels ={'email':"Email"}

	def __init__(self,*args,**kwargs):
		super().__init__(*args,**kwargs)
		self.fields['username'].widget.attrs.update({'class':'form-control'})
		self.fields['first_name'].widget.attrs.update({'class':'form-control'})	
		self.fields['last_name'].widget.attrs.update({'class':'form-control'})
		self.fields['email'].widget.attrs.update({'class':'form-control'})


 