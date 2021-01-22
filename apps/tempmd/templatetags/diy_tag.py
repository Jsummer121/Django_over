# -*- coding: utf-8 -*-
# @Author  : summer
from datetime import datetime
from django.template import Library
from django.template.loader import get_template

register = Library()


# 使用装饰器注册
# @register.simple_tag(name="currtag")
# def current_time(format_str):
# 	now = datetime.now().strftime(format_str)
# 	return now


# 使用上下文
@register.simple_tag(name="currtag", takes_context=True)
def current_time(context):
	now = datetime.now().strftime(context["format_str"])
	return now


# 直接注册
# register.simple_tag(current_time, name="currtag")


@register.inclusion_tag('tempmd/show_list_as_ul.html')
def show_list_as_ul(value):  # 定义一个函数,接收模板变量
	return {'ls': value}  #


# t = get_template('tempmd/show_list_as_ul.html')  # 模板渲染
# register.inclusion_tag(t)(show_list_as_ul)

