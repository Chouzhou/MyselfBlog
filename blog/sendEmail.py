# -*- coding: utf-8 -*-
from django.core.mail import EmailMessage
from django.template import loader
# 异步IO
import asyncio
from Social_Blog.settings import EMAIL_HOST_USER  # 项目配置邮件地址，请参考发送普通邮件部分

# 异步发送邮件


@asyncio.coroutine
def send_html_mail(recipient_list, paramters, user, text_email):
    subject = '验证邮箱'
    html_content = loader.render_to_string(
        text_email,  # 需要渲染的html模板
        {'paramters': paramters,  # 参数
         'user': user
         }
    )
    msg = EmailMessage(subject, html_content, EMAIL_HOST_USER, recipient_list)
    msg.content_subtype = "html"  # Main content is now text/html
    yield from msg.send()
    return True
