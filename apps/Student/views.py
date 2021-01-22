import os
from datetime import datetime

from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

from DjangoModel.settings import MEDIA_ROOT


def login(request):
	num = request.COOKIES.get("num")
	if num:
		num = int(num) + 1
	else:
		num = 1
	if request.method == "POST":
		username = request.POST.get("username")
		password = request.POST.get("password")
		if username == "summer" and password == "summer":
			return HttpResponse("登陆成功")

	response = render(request, 'Student/login.html', context={
		"num": num,
	})
	response.set_cookie("num", num)
	return response


def fileup(request):
	if request.method == "POST":
		# file = request.FILES.get('file')  # 获取一个文件
		files = request.FILES.getlist('file')  # 获取多个文件
		
		# 将每天的文件放到每天的文件夹
		day_dir = datetime.now().strftime("%Y%m%d")
		dir_path = os.path.join(MEDIA_ROOT, day_dir)
		if not os.path.exists(dir_path):  # 查看文件夹是否存在，如果不存在则创建
			os.mkdir(dir_path)
		
		# 添加一张图片
		# file_path = os.path.join(dir_path, file.name)  # 将文件名拼接到medai路径
		# with open(file_path, 'wb') as f:
		# 	for line in file.chunks():  # 上传文件过大时，将文件自动分块
		# 		f.write(line)
		
		# 添加多张图片
		for file in files:
			file_path = os.path.join(dir_path, file.name)  # 将文件名拼接到medai路径
			with open(file_path, 'wb') as f:
				for line in file.chunks():  # 上传文件过大时，将文件自动分块
					f.write(line)
	return render(request, 'Student/fileup.html')


def myview(request):
	return HttpResponse("ok")


class MyView(View):
	
	def get(self, request):
		return HttpResponse("OK")
	
	def post(self, request):
		pass

