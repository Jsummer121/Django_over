from django.urls import path
from . import views

app_name = "tempmodel"

urlpatterns = [
	# path('', views.test1)  # 回顾和理解template
	path("index2", views.index),  # 基础的模板测试
	path("filter", views.test2),  # 使用过滤器的模板测试
	path("login", views.login, name="login"),  # 使用bootstrap
	path("tag", views.test3, name="tag"),  # 使用模板标签的测试
	path("detail/<name>", views.detail, name="detail"),  # 学生详情页面
	path("extend", views.test4, name="extend"),  # 模板的继承和引用测试
	path("diyfilter", views.test5, name="diyfilter"),  # 自定义模板过滤器
	path("diytag", views.test6, name="diytag"),  # 自定义标签
	path("", views.test7, name="addmodel"),  # 将stu由字典变成字符串
]
