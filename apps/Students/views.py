from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.db.models import Q
from django.core.paginator import Paginator
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required
from django.urls import reverse
from django.views import View
from django.views.generic import ListView, DetailView

from .models import Student, Grade, StudentDetail
from .forms import RegisterForm, StudentDetailForm, StudentForm
import math
from django.utils.decorators import method_decorator
# Create your views here.


@permission_required("student.view_student", raise_exception=True)
@login_required
def studets_list(request):
	# if not request.user.has_perm("student.view_student"):
	# 	return HttpResponse("你无权访问")
	
	# # 限制登录
	# if not request.user.is_authenticated:  # 未登录用户访问，返回登录页面
	# 	return redirect(reverse("students:login")+"?next={}".format(request.path_info))
	# 	# login/?next=student_list
	
	section = "学生列表"

	# 查询功能
	search = request.GET.get("search", "").strip()
	if search:
		if search.isdigit():
			stu = Student.objects.filter(Q(qq=search) | Q(phone=search), is_delete=False)
		else:
			stu = Student.objects.filter(name=search, is_delete=False)
	else:
		stu = Student.objects.filter(is_delete=False)
	
	stu = stu.order_by("-c_time")
	# 实现分页:
	# 数据总量
	total_num = stu.count()
	# 每页数据，如果没有数据，就使用默认值为10
	per_page = request.GET.get("per_page", 10)
	# 当前页码
	page = request.GET.get("page", 1)
	
	paginator = Paginator(stu, per_page)
	sts = paginator.get_page(page)
	total_page = paginator.num_pages
	
	return render(request, 'Students/students_list.html', context={
		"section": section,
		"students": sts,
		"search": search,
		"per_page": per_page,
		"total_page": total_page,
		"page": page,
	})


def student_detail(request, pk):
	section = "学生详情"
	student = Student.objects.get(pk=pk)
	return render(request, 'Students/student_detail.html', context={
		"section": section,
		"student": student,
	})


def student_add(request):
	if request.method == "GET":
		section = "添加学生"
		return render(request, "Students/student_detail.html", context={
			"section": section,
		})
	
	if request.method == "POST":
		# 接收传过来的数据，并保存到数据库
		# 1.获取学生信息
		data = {
			"name": request.POST.get("name"),
			"age": request.POST.get("age"),
			"sex": request.POST.get("sex"),
			"qq": request.POST.get("qq"),
			"phone": request.POST.get("phone"),
			"grade_id": request.POST.get("grade"),
		}
		student = Student.objects.create(**data)
		# 获取学生详情并保存数据库
		StudentDetail.objects.create(
			college=request.POST.get("college"),
			student=student,
		)
		return redirect("students:students_list")


def student_delete(request, pk):
	student = Student.objects.get(pk=pk)
	student.is_delete = True
	student.save()
	return redirect("students:students_list")


def student_edit(request, pk):
	section = "修改学生信息"
	student = Student.objects.get(pk=pk)
	if request.method == "GET":
		return render(request, "Students/student_detail.html", context={
			"section": section,
			"student": student,
		})
	if request.method == "POST":
		# 学生列表
		# 获取grade实例
		grade_id = request.POST.get("grade")
		try:
			grade = Grade.objects.get(pk=grade_id)
		except:
			grade = None
		
		student.name = request.POST.get("name")
		student.age = request.POST.get("age")
		student.sex = request.POST.get("sex")
		student.qq = request.POST.get("qq")
		student.phone = request.POST.get("phone")
		# student.grade_id = request.POST.get("grade")  # 第一种，使用id方法
		student.grade = grade  # 第二种：使用表关联法
		
		
		# 学生详情
		try:
			student_detail = student.studentdetail  # 反向
		except:
			student_detail = StudentDetail()  # 正向：空实例
			student_detail.student = student
		
		student_detail.college = request.POST.get("college")
		
		student_detail.save()
		student.save()
		return redirect("students:students_list")


# 测试session
def login_s(request):
	if request.method == "POST":
		name = request.POST["name"]
		password = request.POST["password"]
		if name == "summer" and password == "summer":
			# 将用户名存储到session中，
			request.session["name"] = name
			request.session.set_expiry(10)  # 设置过期时间，如果不设置默认关闭页面时清空
			return redirect("students:index")
	return render(request, "Students/login.html")


def index(request):
	name = request.session.get("name", "游客")  # 获取name的值，如果没有则默认为空
	return render(request, "Students/index.html", context={
		"name": name,
	})


def logout_s(request):
	request.session.flush()
	return redirect("students:index")


def register(request):
	# 将from表单从后台往前台传
	if request.method == "GET":
		form = RegisterForm()  # 没有数据

	if request.method == "POST":
		form = RegisterForm(request.POST)  # 带前面返回的数据
		
		if form.is_valid():  # 实现校验，如果成功返回True
			# 一旦通过调用 `is_valid()` 验证成功（ `is_valid()` 返回 `True` ），已验证的表单数据将被放到 `form.cleaned_data` 字典中。这里的数据已经很好的为你转化为Python类型。
			password = form.cleaned_data.get("password")
			password_repeat = form.cleaned_data.get("password_repeat")
			if password == password_repeat:
				return redirect("students:students_list")
			
	return render(request, "Students/register.html", context={"form": form})


def detail_form(request, pk):
	section = "学生信息修改"
	student = Student.objects.get(pk=pk)
	form = StudentForm(instance=student)  # 指定实例对象
	try:
		detail_form = StudentDetailForm(instance=student.studentdetail)
	except:  # 学生没有详情
		student_detail = StudentDetail()
		student_detail.student = student
		student_detail.save()
		detail_form = StudentDetailForm(instance=student_detail)
		
	if request.method == "POST":
		form = StudentForm(request.POST,instance=student)
		detail_form = StudentDetailForm(request.POST, instance=student.studentdetail)
		
		if form.is_valid() and detail_form.is_valid():
			form.save()
			detail_form.save()
			return redirect("students:students_list")
		
	return render(request, "Students/detail_form.html", context={
		"form": form,
		"detail_form": detail_form,
		"section": section,
	})


# 测试auth系统
def login_auth(request):
	next_url = request.GET.get("next", "/students_list")  # 限制登陆,默认跳转学生列表页
	# user = request.user  # 通过request获取当前用户
	if request.user.is_authenticated:  # 判断当前用户是否已登录
		return redirect(next_url)
	
	# 如果没登录，则返回到登陆页面
	if request.method == "POST":
		# 获取用户名和密码
		username = request.POST["name"]
		password = request.POST["password"]
		# 校验用户名和密码
		user = authenticate(username=username, password=password)  # 正确，返回user对象，错误返回None
		if user is not None:
			# 用户信息存放到session里面，并登录
			login(request, user)
			return redirect(next_url)
		
	return render(request, "Students/login.html")


def logout_auth(request):
	logout(request)
	return redirect("students:index")


# 将注册视图改为类视图
class RegisterView(View):
	def get(self, request):
		form = RegisterForm()  # 没有数据
		return render(request, "Students/register.html", context={"form": form})
	
	def post(self, request):
		form = RegisterForm(request.POST)  # 带前面返回的数据
		
		if form.is_valid():
			password = form.cleaned_data.get("password")
			password_repeat = form.cleaned_data.get("password_repeat")
			if password == password_repeat:
				return redirect("students:students_list")
		return render(request, "Students/register.html", context={"form": form})
	

@method_decorator(login_required, name="dispatch")
class StudentListView(ListView):
	section = "学生列表"
	template_name = "Students/students_list.html"
	model = Student
	
	context_object_name = "students"  # 修改前端的默认名，默认为object_list
	
	# @method_decorator(login_required())
	# def dispatch(self, request, *args, **kwargs):
	# 	return super().dispatch(*args, **kwargs)
	
	# 查询功能
	def get_queryset(self):  # 实现过滤部分
		search = self.request.GET.get("search", "").strip()
		per_page = int(self.request.GET.get("per_page", 10))
		self.paginate_by = per_page
		if search:
			if search.isdigit():
				stu = Student.objects.filter(Q(qq=search) | Q(phone=search), is_delete=False)
			else:
				stu = Student.objects.filter(name=search, is_delete=False)
		else:
			stu = Student.objects.filter(is_delete=False)
		
		students = stu.order_by("-c_time")
		self.students = students
		self.search = search
		return students
	
	def get_context_data(self, *, object_list=None, **kwargs):  # 使用上下文
		context = super().get_context_data(**kwargs)
		context["section"] = self.section
		context["search"] = self.search
		context["per_page"] = self.paginate_by
		context['total_page'] = math.ceil(self.students.count()/self.paginate_by)
		context["page"] = self.request.GET.get("page", 1)
		return context


class StudentDetailView(DetailView):
	template_name = "Students/student_detail.html"
	model = Student  # 模型
	
	context_object_name = "student"
	section = "学生详情"
	
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context["section"] = self.section
		return context
	
	
	

