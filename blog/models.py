# -*- coding:utf-8 -*-
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

# 用户表


class User(AbstractUser):
    mobile = models.CharField(
        max_length=11, blank=True, null=True, unique=True, verbose_name='手机号码')
    is_active = models.BooleanField(default=False)

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = verbose_name
        ordering = ['-id']

    def __str__(self):
        return self.username

    # def get_absolute_url(self):
    #     return '127.0.0.1:8000/account/verify_email/'
# 日志


class Category(models.Model):
    pass
# 日志分类


class Tag(models.Model):
    pass
