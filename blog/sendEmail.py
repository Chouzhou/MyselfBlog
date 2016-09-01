# -*- coding: utf-8 -*-
from django.core.mail import EmailMessage
from django.template import loader

from Social_Blog.settings import EMAIL_HOST_USER  # 项目配置邮件地址，请参考发送普通邮件部分


def send_html_mail(recipient_list, paramters):
    subject = '验证邮箱'
    html_content = loader.render_to_string(
        'email/verify_email.html',  # 需要渲染的html模板
        {'paramters': paramters  # 参数
         }
    )
    msg = EmailMessage(subject, html_content, EMAIL_HOST_USER, recipient_list)
    msg.content_subtype = "html"  # Main content is now text/html
    msg.send()
    return True

# send_html_mail(subject, html_content, [收件人列表]):
