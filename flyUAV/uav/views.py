from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

# Create your views here.

def getLoginPage(request):
    return render(request,'login/login.html')

def getRegisterPage(request):
    return render(request,"register/register.html")
    

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
           return render(request, "login.html",{'error':'Kullanıcı Adı vey Parola hatalı', 
                                                })
    return render(request,'login/login.html')