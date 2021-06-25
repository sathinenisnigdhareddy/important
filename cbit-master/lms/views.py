from django.shortcuts import render,redirect
from .forms  import *
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .models import *
from django.http import HttpResponse
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from .decorators import  allowed_users, admin_only,student_only
# Create your views here.
def registerPage(request):

	form = CreateUserForm()
	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		username = request.POST.get('username')
		semister=request.POST.get('semister')
		branch=request.POST.get('branch')
		year=request.POST.get('year')
		print('username=',username,'semister=',semister,'branch=',branch,'year=',year)
		if form.is_valid():
			user = form.save()
			stu_obj=stud_details.objects.create(semister=semister,branch=branch,username=username)
			stu_obj.save()
			group = Group.objects.get(name='student')
			user.groups.add(group)


			
			

			messages.success(request, 'Account was created for ' + username)

			return redirect('login')
		

	context = {'form':form}
	return render(request, 'register.html', context)
def loginpage(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password =request.POST.get('password')

		user = authenticate(request, username=username, password=password)

		if user is not None:
			login(request, user)
			return redirect('dashboard')
		else:
			messages.info(request, 'Username OR password is incorrect')

	context = {}
	return render(request, 'login1.html')


@login_required(login_url='login')

def dashboard(request):
	return render(request,'dashboard.html')
def logoutUser(request):
	logout(request)
	return redirect('login')

@login_required(login_url='login')
def course_info(request):

	obj=stud_details.objects.all()
	obj2=Courses.objects.all()
	obj1=obj.filter(username=request.user.username)
	if(len(obj1)>0):
		obj3=obj1[0]
		branch=obj3.branch
		semister=obj3.semister
		courses=obj2.filter(branch=branch,semister=semister)
		print('courses',courses)
		content={'courses':courses}
		return render(request,'courses_list.html',content)
	

@login_required(login_url='login')
def view_course(request,pk):
	obj=Course_details.objects.all()
	topics=obj.filter(subject=pk)
	content={'topics':topics}
	return render(request,'topics_list.html',content)


@login_required(login_url='login')
def admin_view(request):
	return render(request,'admin_dashboard.html')

@login_required(login_url='login')
def staff_view(request):
	return render(request,'staff_dashboard.html')


@login_required(login_url='login')
def all_courses(request):
	courses=Courses.objects.all()
	list=[]
	for i in courses:
		if(i.sub1 not in list):
			list.append(i.sub1)
		if(i.sub2 not in list):
			list.append(i.sub2)
		if(i.sub3 not in list):
			list.append(i.sub3)
		if(i.sub3 not in list):
			list.append(i.sub3)
	content={'list':list}
	return render(request,'all_courses.html',content)

@login_required(login_url='login')
def tutorials(request,pk):

	
	obj=lecture_files.objects.all()
	obj1=obj.filter(topic=pk)
	print('objects=',obj1)
	content={'files':obj1}
	return render(request, 'tutorials.html',content)
	
@login_required(login_url='login')
def add_tutorials(request):
	form = lecture_Form()
	if(request.method=='POST'):
		print('hello')
		form = lecture_Form(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return HttpResponse('success')
	context = {'form':form}
	return render(request, 'tutorial_form.html', context)




	

