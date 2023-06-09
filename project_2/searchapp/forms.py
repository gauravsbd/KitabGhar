from django.forms import ModelForm
from .models import searchfield
from django import forms

class searchform(ModelForm):
	password = forms.CharField(widget=forms.PasswordInput)
	class Meta:
		model = searchfield
		fields = '__all__'
		# Book_Name = forms.CharField(widget=forms.TextInput(attrs={'class': 'from-control'}))