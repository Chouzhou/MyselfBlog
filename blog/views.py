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
from django.core.mail import send_mail
from Social_Blog.settings import EMAIL_HOST_USER
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
    return render(request, 'login.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if not user:
            return render(request, 'login.html', {'info': '密码错误或者用户名错误'})
        auth.login(request, user)
        # request.session['user_id'] = user.id
        return HttpResponseRedirect('/')
    return render(request, 'login.html')


# 发送验证邮件


def emailVerify(username, email):
    token_confirm = Token(SECRET_KEY)
    token = token_confirm.generate_validate_token(username)
    user = User.objects.get(username=username)
    print(token)
    send_success = send_html_mail([email, ], token, user)
    return True
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
        send_success = emailVerify(username, email)
        if send_success:
            # request.session['info'] = '发送成功，请到自己的邮箱验证'
            return render(request, 'login.html', {'info': '发送成功，请到自己的邮箱验证'})
    return render_to_response('register.html')
# 验证邮箱


def verify_email(request, argv):
    # try:
    token_confirm = Token(SECRET_KEY)
    print(argv)
    username = token_confirm.confirm_validate_token(argv)
    # except:
    #     return HttpResponse(u'对不起，验证链接已经过期')
    try:
        print(username)
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        return HttpResponse(u'对不起，您所验证的用户不存在，请重新注册')
    if user.is_active:
        return render(request, 'login.html', {'info': '该用户已激活'})
    user.is_active = True
    user.save()
    return render(request, 'login.html', {'info': '激活成功请登录'})

# 退出登录


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')
