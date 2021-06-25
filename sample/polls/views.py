
from django.shortcuts import render,redirect,get_object_or_404
from .forms  import *
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

from django.http import HttpResponse
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required

import requests
from datetime import datetime,date,timedelta
from .models import *
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib.staticfiles import finders
# Create your views here.
def registerPage(request):

	form = CreateUserForm()
	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		username = request.POST.get('username')
		semister=request.POST.get('semister')
		branch=request.POST.get('branch')
		email=request.POST.get('email')
		first_name=request.POST.get('first_name')

		print('username=',username,'semister=',semister,'branch=',branch)
		if form.is_valid():
			user = form.save()
			
			messages.success(request, 'Account was created for ' + username)

			return redirect('login')
		

	context = {'form':form}
	return render(request, 'register.html', context)
def loginpage(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password =request.POST.get('password')
		smcmember=request.POST.get('smcmember')
		print('smcmember',smcmember)
		objs=CustomUser.objects.all()
		obj1=objs.filter(username=160119733113)
		print('hello',obj1)
		print('details',obj1[0].smcmember)
	
		user = authenticate(request,smcmember=smcmember, username=username, password=password)

		if user is not None:
			login(request, user)
			return redirect('dashboard')
		else:
			messages.info(request, 'Username OR password is incorrect')
	
	context = {}
	return render(request, 'login.html')
def dashboard(request):

	return render(request,'dashboard.html')
