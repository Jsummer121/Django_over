import time

from django.shortcuts import redirect
from django.http import HttpResponse, Http404, HttpResponseNotFound


# Create your views here.


def demo(request, n_id=1):
	res = str(n_id) + "这是一个测试app视图"
	return HttpResponse(res)


def demo2(request, name):
	res = "本人的名字是:"+name
	return HttpResponse(res)


def demo3(request, name, age):
	if isinstance(age, int):
		res = "本人名字是：" + name + "，年龄是：" + str(age)
		return HttpResponse(res)
	else:
		return HttpResponse("传入的数字有误！！！")
	

def demo4(request, year):
	res = "今年是：%s年" % year
	return HttpResponse(res)


def stu(request, name):
	return HttpResponse('{}是学生'.format(name))


def index(request):
	return HttpResponse("这是主页。。。。")


def login(request, name, passwd):
	if name == "summer" and passwd == "123456":
		return redirect('demo:index')
	else:
		# raise Http404("username wrong!!!")  # 发出报错信息
		return HttpResponseNotFound('<h1>Page not found</h1>')
