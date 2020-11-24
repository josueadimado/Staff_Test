from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from curriculum.models import Indicator
import json
from django.views.decorators.csrf import csrf_exempt
from .models import CustomUser
from curriculum.models import Result,ResultSection
from random import choice
from django.core.mail import send_mail
from django.template.loader import render_to_string
from accounts.models import Email
import os



BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def gen_referral(length):
    token = ''.join([choice('ABCDEFGHIabcdefgJKLMNOPQRSTUVWXYZhijklmnopqrstuvwxyz0123456789') for i in range(length)])
    return token

def email_users_only_emails(emails,email_subject,extra_args):
    for email in emails:
        email = email
        welcome_mail = Email.objects.get(subject=email_subject)
        path = os.path.join(BASE_DIR, 'accounts/templates/')
        email_html = open(path+"welcome_email.html", "w+")
        email_txt = open(path+"welcome_email.txt", "w+")
        email_html.write(welcome_mail.body)
        email_txt.write(welcome_mail.text)
        email_html.close()
        email_txt.close()
        msg_plain = render_to_string('welcome_email.txt',extra_args)

        msg_html = render_to_string('welcome_email.html', extra_args)
        subject = welcome_mail.subject
        send_mail(
        subject,
        msg_plain,
        'pythonwithellie@gmail.com',
        [email],
        html_message=msg_html,
        fail_silently=False,)

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
    if request.method == "GET":
        template_name = "accounts/forgot-password.html"
        args = {}
        return render(request,template_name,args)
    try:
        email = request['email']
    except Exception as e:
        messages.error(request,str(e)+" is required")
        return redirect("/accounts/forgot-password/")
    else:
        try:
            user = CustomUser.objects.get(email=email)
        except:
            messages.error(request,"We could not find your account, check the email")
            return redirect("/accounts/forgot-password/")
        else:
            token = gen_referral(30)
            user.recover_token = token
            user.save()
            try:
                email_users_only_emails([email],"Forgot Password",{"user":user,"token":token})
            except:
                pass
            messages.success(request,"Please check your mail for further instructions")
            return redirect("/accounts/forgot-password/")
        return redirect("/accounts/forgot-password/")
    return redirect("/accounts/forgot-password/")
            
            
        
     


def register(request):
    if request.method == "GET":
        template_name = "accounts/register.html"
        args = {}
        return render(request,template_name,args)
    try:
        username = request.POST["username"]
        full_name = request.POST["full_name"]
        email = request.POST["email"]
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
            return redirect('/accounts/login/')
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
