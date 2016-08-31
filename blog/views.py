# -*- coding:utf-8 -*-
from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
# 额外需要导入的模块
# 视图函数中给render_to_response增加一个参数:context_instance=RequestContext(request)
from django.template import RequestContext
from blog.models import User
# from django.contrib.auth import logout, login, authenticate
from django.contrib import auth
from blog.create_token import Token
from Social_Blog.settings import SECRET_KEY
from blog.sendEmail import send_html_mail
# from django.views.decorators.csrf import csrf_protect
# Create your views here.

# 主页


def index(request):
    # session获取用户id
    if request.user.is_authenticated():
        return render(request, 'index.html', {'user': request.user})
    return render_to_response('index.html')
# 登录


def login_form(request):
    error_info = request.session.get('error', '')
    if error_info:
        return render(request, 'login.html', {'error': error_info})
    return render(request, 'login.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if not user:
            request.session['error'] = '密码错误或者用户名错误'
            return HttpResponseRedirect('/account/login_form/')
        auth.login(request, user)
        # request.session['user_id'] = user.id
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
        # 发送验证邮箱邮件
        token_confirm = Token(SECRET_KEY)
        token = token_confirm.generate_validate_token(username)
        send_success = send_html_mail([email, ], token)
        if send_success:
            return HttpResponseRedirect('/account/login/', {'info': '发送成功，请到自己的邮箱验证'})
    return render_to_response('register.html')
# 退出登录


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')
