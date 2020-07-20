from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages

# Create your views here.
def login(request):
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
    template_name = "accounts/test.html"
    args = {}
    return render(request,template_name,args)
