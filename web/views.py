# -*- coding:utf-8 -*-
from django.shortcuts import render,HttpResponse,redirect
from web import  models
from django.contrib.sessions.backends.db import SessionStore
# Create your views here.
import  json


def auth(func):
    def inner(request,*args,**kwargs):
        is_login = request.session.get('is_login')
        if is_login:
            return func(request,*args,**kwargs)
        else:
            return  redirect('login.html')
    return inner


def  login(request):
    msg = ''
    if request.method == 'POST':
        user = request.POST.get('email')
        pwd = request.POST.get('password')
        if user is None or  pwd is None:
            msg = u"请输入邮箱帐号和密码"
            return render(request, 'login.html', {'msg': msg})
        else:
            c = models.UserProfile.objects.filter(email= user,password=pwd).count()
            if c:
                request.session['is_login'] = True
                request.session['username'] = models.UserProfile.objects.get(email=user).name
                return redirect('/')
            else:
                msg =u"用户名或者密码错误"
    return   render(request,'login.html',{'msg':msg})

def logout(request):

    request.session.clear()
    return redirect('/')

@auth
def index(request):
    user = request.session.get('username')
    return  render(request,'index.html',{'user':user})
@auth
def host(request):
    host_list = models.Host.objects.all()
    return render(request,'host.html',{'host_list':host_list})







def test1(request):
    return render(request,'1.html')
def test2(request):
    return render(request,'2.html')
def test3(request):
    return render(request,'3.html')
