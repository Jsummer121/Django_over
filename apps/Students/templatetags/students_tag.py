# -*- coding: utf-8 -*-
# @Author  : summer
from Students.models import Grade
from django import template

register = template.Library()


@register.inclusion_tag("Students/grade_option.html")
def grade_option(student):
	grades = Grade.objects.all()
	return {
		"grades": grades,
		"student": student}


@register.inclusion_tag("Students/pagination.html", takes_context=True)
def pagination_html(context):
	total_page = context["total_page"]  # 页码总数
	per_page = context["per_page"]  # 每页的数量
	page = int(context["page"])  # 当前页
	num = 1  # 当前页左右各显示几页
	
	page_list = list()
	# 第一部分：左边和当前页
	# 不显示或不能完全显示:范围（1-当前页）
	if page - num <= 0:
		for i in range(1, page+1):
			page_list.append(i)
	else:
		# 能完全显示
		for i in range(page-num, page+1):
			page_list.append(i)
	
	# 第二部分：右边部分
	# 不显示或不能完全显示：范围（当前页 + 1,total_page）
	if page + num >= total_page:
		for i in range(page + 1, total_page+1):
			page_list.append(i)
	else:
		for i in range(page+1, page + num + 1):
			page_list.append(i)
	return {
		"page_list": page_list,
		"page": page,
		"per_page": per_page,
		"total_page": total_page,
	}


@register.simple_tag()
def add_class(field, class_str):
	return field.as_widget(attrs={"class": class_str})
