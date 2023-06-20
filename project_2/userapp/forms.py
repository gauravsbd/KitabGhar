# from django import forms
# from django.forms import ModelForm
# from .models import loginmodel
# from .models import signupmodel
# from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import userinfomodel
from django.forms import ModelForm




# class loginform(ModelForm):
# 	class Meta:
# 		model = loginmodel
# 		fields = '__all__'
		

# class loginform(AuthenticationForm):
#     class Meta:
#         model = loginmodel
#         fields = ['username', 'password']
#         widgets = {
#             'password': forms.PasswordInput(),
#         }
class signupform(UserCreationForm):
	password2 = forms.CharField(label='Confirm password (again)', widget=forms.PasswordInput())
	class Meta:	
		model = User
		fields = [ 'username','first_name','last_name','email',]
		labels ={'email':"Email"}
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