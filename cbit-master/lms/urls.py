from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
app_name:'account'
urlpatterns = [
   
    path('',views.loginpage,name='login'),
    path('register/', views.registerPage,name="register"),
    path('dashboard', views.dashboard,name="dashboard"),
    path('course_info', views.course_info,name="course_info"),
    path('view_course/<str:pk>/', views.view_course, name="view_course"),
    path('admin_view', views.admin_view,name="admin_view"),
    path('staff_view', views.staff_view,name="staff_view"),
    path('all_courses', views.all_courses,name="all_courses"),
    path('tutorials/<str:pk>/', views.tutorials,name="tutorials"),
   path('add_tutorials', views.add_tutorials,name="add_tutorials"),
          path('reset_password/',
     auth_views.PasswordResetView.as_view(template_name="password_reset.html"),
     name="reset_password"),

    path('reset_password_sent/', 
        auth_views.PasswordResetDoneView.as_view(template_name="password_reset_sent.html"), 
        name="password_reset_done"),

    path('reset/<uidb64>/<token>/',
     auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_form.html"), 
     name="password_reset_confirm"),

    path('reset_password_complete/', 
        auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_done.html"), 
        name="password_reset_complete"),
    path('password-change/', auth_views.PasswordChangeView.as_view(success_url=reverse_lazy('password_change_done')), name='password_change'),


    path('logout/', views.logoutUser, name="logout"),

    ]
