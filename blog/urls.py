# -*- coding:utf-8 -*-
"""Social_Blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
# from blog.views import login_form, register_form, login, register, logout, verify_email, verify_resetPwd_email, resetPwd_email, reset_pwd
from blog.views import *
urlpatterns = [
    url(r'^login_form/', login_form, name='login_form'),
    url(r'^register_form/', register_form, name='register_form'),
    url(r'^login/', login, name='login'),
    url(r'^register/', register, name='register'),
    url(r'^logout/', logout, name='logout'),
    url(r'^verify_email/(?P<argv>\w+.[-_\w]*\w+.[-_\w]*\w+)/',
        verify_email, name='verify_email'),
    # 重设密码
    url(r'^verify_resetPwd_email/(?P<argv>\w+.[-_\w]*\w+.[-_\w]*\w+)/',
        verify_resetPwd_email, name='verify_resetPwd_email'),
    url(r'^resetPwd_email/', send_reset_pwd, name='resetPwd_email'),
    url(r'^reset_pwd/', reset_pwd, name='reset_pwd'),
    url(r'^modify_pwd/', modify_pwd, name='modify_pwd'),
]
