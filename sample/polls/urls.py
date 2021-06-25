from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
app_name:'account'
urlpatterns = [
   
    
    path('register/', views.registerPage,name="register"),
    path('login/', views.loginpage,name="login"),
    path('dashboard/', views.dashboard,name="dashboard"),

]