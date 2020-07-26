from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from curriculum.models import Indicator

# Create your views here.
def tologin(request):
    if request.user.is_authenticated:
        ind = Indicator.objects.first()
        return redirect('/accounts/test/{}/'.format(ind.code))
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

def next(li,element):
    running = True
    idx = li.index(element)
    while running:
        thiselem = li[idx]
        idx = (idx + 1) % len(li)
        nextelem = li[idx]
        if idx == (len(li) - 1):
            return [nextelem,True]
        return [nextelem,False]


def test(request,code):
    # pull indicators here
    template_name = "accounts/test.html"
    all_ids = [i.code for i in Indicator.objects.all()]
    all_ids.insert(0,"first")
    my_next = next(all_ids,code)
    try:
        indicator = Indicator.objects.get(code=code)
    except:
        return redirect("/accounts/results/")
    args = {}
    args['indicator'] = indicator
    args['next'] = my_next[0]
    args['total'] = len(indicator.questions.all())
    return render(request,template_name,args)


def results(request):
    template = "accounts/results.html"
    args = {}
    return render(request,template,args)


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
                ind = Indicator.objects.first()
                return redirect('/accounts/test/{}/'.format(ind.code))
            else:
                messages.error(request,"Please check username and password well")
                return redirect('/accounts/login/')
    else:
        args = {}
        args['title']='Login'
        return render(request,'accounts/login.html',args)

