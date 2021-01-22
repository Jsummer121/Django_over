from django.contrib import admin
from .models import Student, StudentDetail

# Register your models here.


class StudentAdmin(admin.ModelAdmin):
	list_display = ["id", "name", "sex", "qq", "phone"]  # 设置显示的内容
	list_display_links = ["name", "sex"]  # 设置可以实现跳转的内容
	list_filter = ["sex"]  # 添加过滤器
	search_fields = ["name", "qq", "phone"]  # 添加搜索功能
	list_per_page = 5  # 分页功能
	
	# 详情页
	# fields = ["age", "qq", "phone"]  # 显示信息
	fieldsets = [  # 分组设置
		(None, {"fields": ["age", "sex"]}),
		("详细信息", {"fields": ["qq", "phone", "grade"]}),
		('设置信息', {"fields": ["is_delete"]})
	]


admin.site.register(Student, StudentAdmin)
admin.site.register(StudentDetail)
