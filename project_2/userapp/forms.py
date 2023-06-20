
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
<<<<<<< HEAD

	def __init__(self,*args,**kwargs):
		super().__init__(*args,**kwargs)
		self.fields['username'].widget.attrs.update({'class':'form-control'})
		self.fields['first_name'].widget.attrs.update({'class':'form-control'})	
		self.fields['last_name'].widget.attrs.update({'class':'form-control'})
		self.fields['email'].widget.attrs.update({'class':'form-control'})


 
=======
		# widgets = {  
        #       'Contact_No':forms.NumberInput(),
        #       'Password': forms.PasswordInput(),
        #       'Email': forms.EmailInput()
        # }        
class userinfoform(ModelForm):
	class Meta:
		model = userinfomodel
		fields = '__all__'	
		# fields=[ 'Name','Phone_Number','Address','user','Profile_photo']	
>>>>>>> 2e627352b06550f617ba7c4191e7517c95d33300
