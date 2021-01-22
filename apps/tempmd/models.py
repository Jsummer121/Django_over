from django.db import models


# Create your models here.
class Student(models.Model):
	name = models.CharField(max_length=20)
	age = models.SmallIntegerField(null=True)
	height = models.SmallIntegerField(null=True)
	sex = models.SmallIntegerField(default=1)
	qq = models.CharField(max_length=20, null=True)
	phone = models.CharField(max_length=20, null=True)
	c_time = models.DateTimeField("创建时间", auto_now_add=True)
	
	def __str__(self):
		return self.name

