from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def tologin(request):
    template_name = "accounts/login.html"
    args = {}
    return render(request,template_name,args)


def forgot(request):
    template_name = "accounts/forgot-password.html"
    args = {}
    return render(request,template_name,args)


def register(request):
    template_name = "accounts/register.html"
    args = {}
    return render(request,template_name,args)

def index(request):
    template_name = "accounts/index.html"
    args = {}
    return render(request,template_name,args)

def test(request):
    # pull indicators here
    template_name = "accounts/test.html"
    args = {}
    return render(request,template_name,args)


def mylogin(request):
    if request.method == "POST":
        try:
            username = request.POST['username']
            password = request.POST['password']
        except Exception as e:
            messages.error(request,str(e))
            return redirect('/accounts/login/')
        else:
            user = authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('/accounts/test/')
            else:
                messages.error(request,"Please check username and password well")
                return redirect('/accounts/login/')
    else:
        args = {}
        args['title']='Login'
        return render(request,'accounts/login.html',args)

