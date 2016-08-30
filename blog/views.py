# -*- coding:utf-8 -*-
from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
# 额外需要导入的模块
# 视图函数中给render_to_response增加一个参数:context_instance=RequestContext(request)
from django.template import RequestContext
from blog.models import User
# from django.views.decorators.csrf import csrf_protect
# Create your views here.

# 主页


def index(request):
    return render_to_response('index.html')
    # , {'user': request.session['user']})
# 登陆


def login_form(request):
    return render(request, 'login.html')


# @csrf_protect
def login(request):
    if request.method == 'POST':
        user = User.objects.filter(username=request.POST[
                                   'username'], password=request.POST['password'])
        # print(user.)
        if not user:
            return HttpResponseRedirect('/login_form/', {'error': '密码错误或者用户名错误'})
        request.session['username'] = request.POST['username']
        return HttpResponseRedirect('/')
    return render_to_response('login.html', context_instance=RequestContext(request))
# 注册


def register_form(request):
    return render(request, 'register.html')


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # email = request.POST['email']
        print(username, password)
        user = User(username=username,
                    password=password,
                    # email=email,
                    )
        user.save()
        return HttpResponseRedirect('/login/')
    return render_to_response('register.html')
