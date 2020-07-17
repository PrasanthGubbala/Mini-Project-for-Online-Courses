"""OnlineCourses URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.views.generic.base import TemplateView
from app import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    #admin panel
    path('admin/',views.admin,name='admin'),
    path('check_admin/',views.check_admin,name='check_admin'),
    path('admin_home/',views.admin_home,name='admin_home'),
    path('schedule_new_class/',views.schedule_new_class,name='schedule_new_class'),
    path('save_course/',views.save_course,name='save_course'),
    path('view_all_courses/',views.view_all_courses,name='view_all_courses'),
    path('delete_course/',views.delete_course,name='delete_course'),
    path('update_course/',views.update_course,name='update_course'),
    path('update_course_save/', views.update_course_save, name='update_course_save'),

    #student panel
    path('',views.student_main,name='student_main'),
    path('student_register/',views.student_register,name='student_register'),
    path('save_student_registration/',views.save_student_registration,name='save_student_registration'),
    path('student_login/',views.student_login,name='student_login'),
    path('student_login_check/',views.student_login_check,name='student_login_check'),
    path('contact_us/',views.contact_us,name='contact_us'),
    path('student_home_cont/',views.student_home_cont,name='student_home_cont'),
    path('enroll_the_course/',views.enroll_the_course,name='enroll_the_course'),
    path('enroll_course/',views.enroll_course,name='enroll_course'),
    path('view_all_enrolled_classes/',views.view_all_enrolled_classes,name='view_all_enrolled_classes'),
]
