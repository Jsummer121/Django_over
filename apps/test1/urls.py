from django.urls import path, re_path
from . import views

app_name = "demo"

urlpatterns = [
	# path('demo', views.demo),  # 不传参，直接使用该函数中的默认参数
	# path('demo/<n_id>', views.demo),  # 传参，使用传入的参数
	# # path('demo/<name>/<age>', views.demo3),  # 传入两个参数无法判断值
	#
	# # 使用转换器，
	# path('demo/<str:name>', views.demo2),  # 规定传入的值
	# path('demo/<str:name>/<int:age>', views.demo3),  # 如果是像这样的，需要先把使用转换器的放前面，然后将能接受所有的都传入（没意义）
	# path('demo/<name>/<age>', views.demo3),  # 传入两个参数无法判断值
	
	# 正则匹配
	# re_path(r'^demo/(?P<year>[0-9]{4})', views.demo4)
	
	# 使用kwargs
	# path('student', views.stu, kwargs={"name": "summer"}),
	
	
	# name属性（反向解析）
	# path("index", views.index, name='index'),
	# path("login", views.login),
	
	# 小实验
	path("index", views.index, name='index'),
	path("login/<name>/<passwd>", views.login, name='login')
]
