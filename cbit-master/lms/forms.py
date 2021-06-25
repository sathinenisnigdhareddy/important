from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import *
from django.forms import ModelForm
class CreateUserForm(UserCreationForm):
	class Meta:
		model=User
		fields=['username','first_name','email','password1','password2']
class lecture_Form(ModelForm):
	class Meta:
		model = lecture_files
		fields = '__all__'
		