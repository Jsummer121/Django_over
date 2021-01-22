# -*- coding: utf-8 -*-
# @Author  : summer
from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

app_name = "students"

urlpatterns = [
	# path("students_list", views.studets_list, name="students_list"),  # 普通写法
	path("students_list", views.StudentListView.as_view(), name="students_list"),  # 类视图写法
	# path("students_list", login_required(views.StudentListView.as_view()), name="students_list"),# 添加装饰器写法
	# path("student_detail/<pk>", views.student_detail, name="student_detail"),
	path("student_detail/<pk>", views.StudentDetailView.as_view(), name="student_detail"),
	path("student_add", views.student_add, name="student_add"),
	path("student_delete/<pk>", views.student_delete, name="student_delete"),
	path("student_edit/<pk>", views.student_edit, name="student_edit"),
	# path("login", views.login, name="login"),  # 原先的
	path("login", views.login_auth, name="login"),  # 测试权限系统
	path("index", views.index, name="index"),
	# path("logout", views.logout, name="logout"),  # 原先的
	path("logout", views.logout_auth, name="logout"),
	# path("register", views.register, name="register"),  # 原来的
	path("register", views.RegisterView.as_view(), name="register"),
	path("detail_form/<pk>", views.detail_form, name="detail_form"),
]
