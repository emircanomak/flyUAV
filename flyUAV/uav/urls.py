from django.contrib import admin
from django.urls import path,include
from .views import getRegisterPage,getHomePage,login_request

app_name="uav"

urlpatterns = [
    path('',login_request),
    path('register/',getRegisterPage),
    path("home/",getHomePage,name="home"),

]
