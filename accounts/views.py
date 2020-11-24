from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from curriculum.models import Indicator
import json
from django.views.decorators.csrf import csrf_exempt
from .models import CustomUser
from curriculum.models import Result,ResultSection

# Create your views here.
def tologin(request):
    if request.user.is_authenticated:
        ind = Indicator.objects.first()
        # return redirect('/accounts/test/{}/'.format(ind.code))
        return redirect('/accounts/index/')
    template_name = "accounts/login.html"
    args = {}
    return render(request,template_name,args)


def forgot(request):
    template_name = "accounts/forgot-password.html"
    args = {}
    return render(request,template_name,args)


def register(request):
    if request.method == "GET":
        template_name = "accounts/register.html"
        args = {}
        return render(request,template_name,args)
    try:
        username = request.POST["username"]
        full_name = request.POST["full_name"]
        email = request.POST["emali"]
        password = request.POST["password"]
    except Exception as e:
        messages.error(request,str(e)+" is required")
    else:
        try:
            user = CustomUser()
            user.username = username
            user.email = email
            user.full_name = full_name
            user.save()
            user.set_password(password)
            user.save()
        except Exception as e:
            messages.error(request,str(e))
        else:
            messages.success(request,"Successfully registered. Please login now.")
            return redirect('/accounts/register/')
   return redirect('/accounts/register/')
    

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
                # return redirect('/accounts/test/{}/'.format(ind.code))
                return redirect('/accounts/index/')
            else:
                messages.error(request,"Please check username and password well")
                return redirect('/accounts/login/')
    else:
        args = {}
        args['title']='Login'
        return render(request,'accounts/login.html',args)


@csrf_exempt
def saveResults(request):
    json_data = json.loads(str(request.body, encoding='utf-8'))
    objects = {}
    for key,val in json_data.items():
        objects[key]=val
    data = {}

    try:
        user = CustomUser.objects.get(username=objects['user'])
    except Exception as e:
        data['success']=False
        data['message']=str(e)
        dump = json.dumps(data)
        return HttpResponse(dump, content_type='application/json')
    # lets create a result
    r = Result()
    r.institution = objects['institution']
    r.comment = objects['comment']
    r.taker = user
    r.save()
    # lets create result for each one
    for each in objects['objects']:
        res = ResultSection()
        res.name = each['y']
        res.mean = each['a']
        res.sd = each['b']
        res.result = r
        res.save()
    data['success']=True
    data['message']="Results saved!"
    dump = json.dumps(data)
    return HttpResponse(dump, content_type='application/json')
