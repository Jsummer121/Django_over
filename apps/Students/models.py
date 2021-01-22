from django.db import models


# Create your models here.
# 模型的简单理解
# class Student(models.Model):
# 	name = models.CharField(max_length=20)  # 对应于mysql的varchar
# 	age = models.SmallIntegerField(null=True)  # 对应于mysql的smallint
# 	sex = models.SmallIntegerField(default=1)  # default是默认值
# 	qq = models.CharField(max_length=20, null=True, unique=True)  # qq和电话虽然是数字，但是我们保存一般使用字符串去保存
# 	phone = models.CharField(max_length=20, null=True, unique=True)
# 	# c_time = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)  # verbose_name用来给该字段添加说明      auto_now_add=True自动填充当前时间)
# 	c_time = models.DateTimeField("创建时间", auto_now_add=True)  # 当然你想完全可以在第一个参数写入名字而省略写verbose_name这个参数名
# 	x_time = models.DateTimeField("修改时间", auto_now=True)  # 修改之后自动保存
#
# 	def __str__(self):
# 		return "这个学生的名字是：%s，年龄为：%d" % (self.name, self.age)


# 表关系的实现
class Student(models.Model):
	"""学生表"""
	name = models.CharField("学生姓名", max_length=20)
	age = models.SmallIntegerField("年龄", null=True)
	SEX_CHOICE = (
		[0, "女"],
		[1, "男"]
	)
	sex = models.SmallIntegerField("性别", choices=SEX_CHOICE, default=1)
	qq = models.CharField("QQ号", max_length=20, unique=True, null=True, error_messages={"unique": "qq号码重复！！"})  # 错误信息提示
	phone = models.CharField("手机号", max_length=20, unique=True, null=True, error_messages={"unique": "电话号码重复"})
	c_time = models.DateTimeField("创建时间", auto_now_add=True)
	# ***与Detail的OneToOneField同样可以写在这里***
	# detail = models.OneToOneField('StudentDetail', on_delete=models.SET_NULL, null=True)  # 当学生详情被删除的时候，这个地方变成null
	# ***与Grade的一对多关系只可以写在这里***
	grade = models.ForeignKey('Grade', on_delete=models.SET_NULL, null=True)  # 如果班级删除，此时这里的值变成null。
	is_delete = models.BooleanField(default=False)  # 来记录一条数据的状态
	
	def __str__(self):
		return "{}-{}".format(self.name, self.age)


class StudentDetail(models.Model):
	"""学生详情表"""
	college = models.CharField("学院", max_length=20)
	student = models.OneToOneField('Student', on_delete=models.CASCADE)  # 随着学生信息的删除，此详情也更着删除


class Grade(models.Model):
	"""班级表"""
	name = models.CharField("班级名称", max_length=20)
	num = models.CharField("班期", max_length=20)
	
	def __str__(self):
		return self.name


class Course(models.Model):
	"""课程表"""
	name = models.CharField("课程名", max_length=20)
	students = models.ManyToManyField("Student", through="Enroll")  # 多对多可以不创建中间表，他自动会生成一个中间表。如果自己写了中间表，此时就需要添加一个through


class Enroll(models.Model):
	"""中间表"""
	student = models.ForeignKey("Student", on_delete=models.CASCADE)
	course = models.ForeignKey("Course", on_delete=models.CASCADE)
	pay = models.FloatField("缴费金额", default=0)
	c_time = models.DateTimeField("缴费时间", auto_now_add=True)
