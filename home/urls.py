from django.contrib import admin
from django.urls import path,include
from home.views import *

urlpatterns = [
    path('',index,name='index'),
    
    path('api/employee/',Employees.as_view(),name='employees'),
    path('api/login',LoginApi.as_view()),

]
