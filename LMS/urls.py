"""LMS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include
from .import views,user_login

from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),


    path('base',views.BASE,name='base'),

    path('404', views.PAGE_NOT_FOUND,name='404'),

    path('',views.HOME,name='home'),

    path('courses',views.SINGLE_COURSE, name='single_course'),
    
    path('courses/filter-data',views.filter_data,name="filter-data"),

    path('course/<slug:slug>/', views.COURSE_DETAILS, name='course_details'),

    path('search', views.SEARCH_COURSE, name='search_course'),
    
    path('contact',views.CONTACT_US, name='contact_us'),

    path('about',views.ABOUT_US, name='about_us'),

    path('accounts/register',user_login.REGISTER,name='register'),

    path('accounts/', include('django.contrib.auth.urls')),
    
    path('doLogin',user_login.DO_LOGIN,name='doLogin'), 

    path('accounts/profile', user_login.PROFILE, name='profile'),

    path ('accounts/profile/update', user_login.PROFILE_UPDATE, name='profile_update'),
    
    path('checkout/<slug:slug>',views.CHECKOUT, name='checkout'),
    
    path('my_course', views.MY_COURSE,name='my_course'),
    
    path('verify_payment', views.VERIFY_PAYMENT, name ='verify_payment'),
    
    path('course/watch-course/<slug:slug>', views.WATCH_COURSE,name='watch_course'),

] + static(settings.MEDIA_URL,document_root =settings.MEDIA_ROOT)
urlpatterns +=staticfiles_urlpatterns()
