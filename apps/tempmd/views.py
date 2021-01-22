from datetime import datetime

from django.shortcuts import render
from django.http import HttpResponse
from .models import Student
from django.template.loader import get_template


# Create your views here.
# 主页视图
def index(request):
	now = datetime.now()  # 获取当前时间
	# now = now.strftime("%Y年%m月%d日 %H:%M:%S")  # 用后台控制时间格式
	return render(request, 'tempmd/index.html', context={
		'now': now,
	})


# 登录视图，使用bootstrap
def login(request):
	return render(request, 'tempmd/sinn-in.html')


# url标签——学生详情
def detail(request, name):
	return HttpResponse("{}同学的详情".format(name))


# 理解模板渲染初级
def test1(request):
	# 1.直接返回html
	# return HttpResponse("<h1>这是tempmodel的第一个测试</h1>")
	
	# 2.使用模板渲染返回
	# t = get_template('tempmd/index.html')
	# html = t.render()
	# return HttpResponse(html)
	
	# 3.正常的返回
	return render(request, 'tempmd/index.html')


# 理解模板过滤器
def test2(request):
	now = datetime.now()  # 获取当前时间
	li = [4, 5, 6]
	stu = {"name": "summer", "age": 20, "hoppy": "football"}
	st = "My name is summer"
	js = "<script>alert('1')</script>"
	return render(request, 'tempmd/test2.html', context={
		"now": now,
		"li":  li,
		"stu": stu,
		"st": st,
		"js": js,
	})


# 理解模板标签
def test3(request):
	stu = [
		{"name": "Summer", "age": 20, "hoppy": "football", "sex": "男"},
		{"name": "July", "age": 20, "hoppy": "photos", "sex": "女"},
		{"name": "April", "age": 20, "hoppy": "eat", "sex": "女"},
		{"name": "Moli", "age": 20, "hoppy": "play", "sex": "女"},
		{"name": "XiaoMing", "age": 20, "hoppy": "basketball", "sex": "男"},
	]
	
	return render(request, 'tempmd/undtag.html', context={
		"students": stu,
	})


def test4(request):
	now = datetime.now()  # 获取当前时间
	return render(request, 'tempmd/extends.html', context={'now': now, })


# 理解自定义模板过滤器
def test5(request):
	stu = [
		{"name": "Summer", "age": 20, "hoppy": "football", "sex": 1},
		{"name": "July", "age": 20, "hoppy": "photos", "sex": 0},
		{"name": "April", "age": 20, "hoppy": "eat", "sex": 0},
		{"name": "Moli", "age": 20, "hoppy": "play", "sex": 0}]

	return render(request, 'tempmd/diyfileter.html', context={"students": stu, })


# 理解自定义标签
def test6(request):
	now = datetime.now()  # 获取当前时间
	stu = [
		{"name": "Summer", "age": 20, "hoppy": "football", "sex": 1, "course": ["python", "web", "java", "c++"]},
		{"name": "July", "age": 20, "hoppy": "photos", "sex": 0, "course": ["python", "web", "java", "c++"]},
		{"name": "April", "age": 20, "hoppy": "eat", "sex": 0, "course": ["python", "web", "java", "c++"]},
		{"name": "Moli", "age": 20, "hoppy": "play", "sex": 0, "course": ["python", "web", "java", "c++"]}
	]
	return render(request, 'tempmd/diytag.html', context={
		"now": now,
		"format_str": "%Y年%m月%d日 %H:%M:%S",
		"students": stu,
	})


# 使用model去修改stu
def test7(request):
	now = datetime.now()  # 获取当前时间
	# stu = [
	# 	{"name": "Summer", "age": 20, "hoppy": "football", "sex": 1, "course": ["python", "web", "java", "c++"]},
	# 	{"name": "July", "age": 20, "hoppy": "photos", "sex": 0, "course": ["python", "web", "java", "c++"]},
	# 	{"name": "April", "age": 20, "hoppy": "eat", "sex": 0, "course": ["python", "web", "java", "c++"]},
	# 	{"name": "Moli", "age": 20, "hoppy": "play", "sex": 0, "course": ["python", "web", "java", "c++"]}
	# ]
	stu = Student.objects.all()
	
	return render(request, 'tempmd/diytag.html', context={
		"now": now,
		"format_str": "%Y年%m月%d日 %H:%M:%S",
		"students": stu,
	})
