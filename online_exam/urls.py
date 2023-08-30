"""online_exam URL Configuration

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
import os
from django.contrib import admin, auth
#from django.conf.urls import re_path
from django.urls import path, include,re_path
from django.conf import settings
from django.conf.urls.static import static
from .views import *
# from ..teacher.views import QuestionList

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
urlpatterns = [
    path('', home,name='home'),
    path('admin/', admin.site.urls,name='admin'),
    re_path(r'^css/(?P<file>.*)$', css, name='css'),
    # path('student/', include('C:\Users\student\Desktop\Python\online_exam\teacher\urls.py')),
    path('teacher/', include((r'teacher.urls','teacher'),namespace='teacher')),
    path('student/', include((r'student.urls','student'),namespace='student')),
    re_path(r'^images/(.*)$',image , name='images'),
    path('contact/', contact,name='contact'),
    path('about/', about,name='about'),
    path('',include((r'main.urls','main'),namespace='main')),

]
