# -*- coding: utf-8 -*-
# @Author  : summer
from django.urls import path
from . import views

app_name = "student"

# 模型理解
urlpatterns = [
	path("login", views.login, name="login"),  # 用户登录测试
	path("fileup", views.fileup, name='fileup'),  # 文件上传测试
	path("my_D", views.myview, name='my_D'),  # 普通视图与类视图
	path("my_V", views.MyView.as_view(), name='my_V'),  # 普通视图与类视图
]
