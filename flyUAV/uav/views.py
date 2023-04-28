from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login ,logout
from django.contrib.auth.decorators import login_required


from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# Create your views here.
from django.contrib.auth.models import User, auth
from django.db.models import Q
from django.http import HttpResponse, Http404, HttpRequest, request
from .serializers import IhaSerializerGet, IhaSerializerPost, IhaSerializerUpdate, ModelSerializer, CategorySerializer, BrandSerializer
from .models import ihaModel, Model, Brand, Category
from django.views.decorators.csrf import csrf_exempt
from rest_framework.permissions import AllowAny
from rest_framework import permissions, viewsets

from django.contrib.auth import authenticate, login,logout

from rest_framework import views
from . import serializers
from rest_framework.decorators import api_view
# Create your views here.

#  Authenticate
def getLoginPage(request):
    return render(request,'login/login.html')

def getRegisterPage(request):

    if request.method=='GET':
        return render(request,"register/register.html")
    else:
        return register(request=request)
    

@login_required(login_url="/")
def getHomePage(request):
    return render (request,"main/main.html")

def login_request(request):
    if request.method == 'POST':
       login_username =  request.POST["login_username"]
       login_password = request.POST["login_password"]

       user = authenticate(request, username=login_username, password = login_password)
       print(login_username)
       print(login_password)
       print(user)
       if user  is not None:
           login(request ,user) 
           return redirect("home/")
       else:
           return render(request, "login/login.html",{'error':'Kullanıcı Adı veya Parola hatalı', 
                                                })
    return render(request,'login/login.html')

#Logout
def custom_logout(request):
    logout(request)
    return redirect("/")

# Crud #

@login_required(login_url="/")
def getAddUav(request):
    return render (request,"crud/addUAV.html")

@login_required(login_url="/")
def getUpdateUav(request,id):
    uav=ihaModel.objects.get(pk=id)
    context={
        "uav":uav,
        "id":id
    }
    return render (request,"crud/updateUAV.html",context=context)

#Register #
@csrf_exempt
def register(request):
    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']


        if User.objects.filter(username=username).exists():
            response_data = {
                "username": "Kullanıcı adı zaten kayıtlı"
            }
            return render(request,'register/register.html',context=response_data)
        else:
            user = User.objects.create_user(username=username, password=password, is_active=True)
            user.save()
            response_data = {
                "success": "Kullanıcı oluşturma başarılı"
            }
            return render(request, 'register/register.html', context=response_data)
    else:
        return render(request,'register/register.html')
# Rest Framework #
class CategoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes_by_action = {'create': [permissions.IsAuthenticated],
                                    'list': [AllowAny]}

    def list(self, request):
        queryset = Category.objects.all()
        serializer = CategorySerializer(queryset, many=True)
        return Response(serializer.data)


class BrandViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    permission_classes_by_action = {'create': [permissions.IsAuthenticated],
                                    'list': [AllowAny]}

    def list(self, request):
        queryset = Brand.objects.all()
        serializer = BrandSerializer(queryset, many=True)
        return Response(serializer.data)


class ModelViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Model.objects.all()
    serializer_class = ModelSerializer
    permission_classes_by_action = {'create': [permissions.IsAuthenticated],
                                    'list': [AllowAny]}

    def list(self, request):
        print(request.GET.get('brand'))
        if request.GET.get('brand') is not None:
            queryset = Model.objects.filter(brand=request.GET.get('brand'))
            serializer = ModelSerializer(queryset, many=True)
            return Response(serializer.data)
        else:
            queryset = Model.objects.all()
            serializer = ModelSerializer(queryset, many=True)
            return Response(serializer.data)

class IhaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = ihaModel.objects.all()
    serializer_class = IhaSerializerGet
    permission_classes_by_action = {'create': [permissions.IsAuthenticated],
                                    'list': [AllowAny]}

    def list(self, request):
        if request.GET.get('brand') is not None:
            queryset = ihaModel.objects.filter(brand__name__icontains=request.GET.get('brand'))
            serializer = IhaSerializerGet(queryset, many=True)
            return Response(serializer.data)
        elif request.GET.get('category') is not None:
            queryset = ihaModel.objects.filter(category__name__icontains=request.GET.get('category'))
            serializer = IhaSerializerGet(queryset, many=True)
            return Response(serializer.data)
        elif request.GET.get('model') is not None:
            queryset = ihaModel.objects.filter(model__name__icontains=request.GET.get('model'))
            serializer = IhaSerializerGet(queryset, many=True)
            return Response(serializer.data)
        elif request.GET.get('search') is not None:
            queryset = ihaModel.objects.filter(Q(brand__name__icontains=request.GET.get('search')) | Q(
                category__name__icontains=request.GET.get('search')) | Q(
                model__name__icontains=request.GET.get('search')) | Q(weight__icontains=request.GET.get('search')))
            serializer = IhaSerializerGet(queryset, many=True)
            return Response(serializer.data)
        else:
            queryset = ihaModel.objects.all()
            serializer = IhaSerializerGet(queryset, many=True)
            return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = IhaSerializerPost(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

    def update(self, request, pk, *args, **kwargs):
        instance = ihaModel.objects.get(pk=pk)
        serializer = IhaSerializerUpdate(instance, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
        else:
            print(serializer.errors)
        return Response(serializer.data)

