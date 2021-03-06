# -*- coding: utf-8 -*-
# @Author  : summer
from django.http import HttpResponseForbidden


def simple_middleware(get_response):  # 同时这个参数名也是不能改动的
	print("初始化设置1")
	
	def middleware(request):
		# 实现只能google浏览器才能访问
		user_agent = request.META.get("HTTP_USER_AGENT")
		if not "chrome" in user_agent.lower():
			return HttpResponseForbidden()
		
		print("处理请求前，执行的代码1")
		response = get_response(request)
		print("处理请求后执行的代码2")
		return response
	return middleware


# 类
class SimpeMiddleWare:
	def __init__(self, get_response):
		self.get_response = get_response
		print("初始化设置2")
	
	def __call__(self, request, *args, **kwargs):
		# 实现只能google浏览器才能访问
		user_agent = request.META.get("HTTP_USER_AGENT")
		if not "chrome" in user_agent.lower():
			return HttpResponseForbidden()
		
		print("处理请求前，执行的代码3")
		response = self.get_response(request)
		print("处理请求后执行的代码4")
		return response
