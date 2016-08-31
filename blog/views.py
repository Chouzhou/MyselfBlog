# -*- coding:utf-8 -*-
from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
# 额外需要导入的模块
# 视图函数中给render_to_response增加一个参数:context_instance=RequestContext(request)
from django.template import RequestContext
from blog.models import User
from django.contrib.auth import logout, login, authenticate
# from django.views.decorators.csrf import csrf_protect
# Create your views here.

# 主页


def index(request):
    # session获取用户id
    user_id = request.session.get('user_id', '')
    if user_id:
        user = User.objects.get(id=user_id)
        return render(request, 'index.html', {'user': user})
    return render_to_response('index.html')
# 登陆


def login_form(request):
    error_info = request.session.get('error', '')
    if error_info:
        return render(request, 'login.html', {'error': error_info})
    return render(request, 'login.html')


# @csrf_protect
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if not user:
            request.session['error'] = '密码错误或者用户名错误'
            return HttpResponseRedirect('/login_form/')
        request.session['user_id'] = user.id
        return HttpResponseRedirect('/')
    return render(request, 'login.html')
# 注册


def register_form(request):
    return render(request, 'register.html')


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        print(username, password, email)
        user = User.objects.create_user(username=username,
                                        password=password,
                                        email=email,
                                        )
        user.save()
        return HttpResponseRedirect('/login/')
    return render_to_response('register.html')
