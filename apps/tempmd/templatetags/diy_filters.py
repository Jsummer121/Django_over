# -*- coding: utf-8 -*-
# @Author  : summer
from django import template

register = template.Library()  # 这里的变量名必须为register


@register.filter()
def to_sex(value, language="zh"):
	change = {
		"zh": ("女", "男"),
		"en": ("Female", "Male"),
	}
	return change[language][value]


# 注册
# def filter(self, name=None, filter_func=None, **flags):因此你是可以为这个过滤器添加一个名字的在这个名字前（如果不加就是函数名)
# register.filter(to_sex)
