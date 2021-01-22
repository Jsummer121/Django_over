# -*- coding: utf-8 -*-
# @Author  : summer
from django import forms
from Students.models import Student, StudentDetail


# 简单表单
class RegisterForm(forms.Form):
	username = forms.CharField(label="用户名", max_length=20)
	password = forms.CharField(
		label="密码",
		max_length=8,
		min_length=6,
		widget=forms.PasswordInput(attrs={"placeholder": "请输入6-8位长的密码"}),  # 添加额外的属性
		error_messages={
			"min_length": "密码长度小于6位",
			"max_length": "密码长度大于8位",
		}  # 设定报错信息
	)
	password_repeat = forms.CharField(label="确认密码", widget=forms.PasswordInput(attrs={"placeholder": "再次输入密码"}))
	
	def clean(self):  # 多字段联合校验
		cleaned_data = super().clean()  # 继承父类
		
		# 增加提示信息
		password = cleaned_data.get("password")
		password_repeat = cleaned_data.get("password_repeat")
		if password != password_repeat:
			msg = "密码不一致"
			self.add_error("password_repeat", msg)
	
	def clean_username(self):  # 单字段校验
		pass


# 模型表单
class StudentForm(forms.ModelForm):
	class Meta:
		model = Student  # 模型
		# fields = "__all__"
		exclude = ["is_delete"]  # 排除字段
		
	def clean_phone(self):
		phone = self.cleaned_data.get("phone")
		if (phone,) in Student.objects.values_list("phone"):
			raise forms.ValidationError("手机号码已经注册，请重新输入！！！")
		return phone


class StudentDetailForm(forms.ModelForm):
	class Meta:
		model = StudentDetail  # 模型
		# fields = "__all__"
		exclude = ["student"]