# -*- coding:utf-8 -*-
from django.db import models
from datetime import datetime
# Create your models here.

# 用户表


class User(models.Model):
    username = models.CharField(max_length=15)
    password = models.CharField(max_length=100)
    # 注册时间
    register_time = models.DateTimeField(auto_now_add=True)
    # 最近登录时间
    last_time = models.DateTimeField(auto_now=True)

# 日志


class Category(models.Model):
    pass
# 日志分类


class Tag(models.Model):
    pass
