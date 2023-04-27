from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from .views import getRegisterPage,getHomePage,getAddUav,getUpdateUav,login_request,BrandViewSet,CategoryViewSet,ModelViewSet,IhaViewSet

app_name="uav"


router=routers.DefaultRouter()
router.register(r'iha',IhaViewSet,basename='Iha')
router.register(r'model',ModelViewSet,basename='Model')
router.register(r'brand',BrandViewSet,basename='Brand')
router.register(r'category',CategoryViewSet,basename='Category')



urlpatterns = [
    path('',login_request),
    path('register/',getRegisterPage),
    path("home/",getHomePage,name="home"),
    path("addUav/",getAddUav),
    path("updateUav/",getUpdateUav),
    path('api/', include(router.urls)),

]
