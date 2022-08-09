from django.db import models
from django.contrib.auth.models import User



class student(models.Model):
	stu_name = models.TextField()
	stu_class = models.TextField()
	phone_number = models.TextField()
	roll_num = models.TextField()


class classroom(models.Model):
	c = models.TextField()
class opt(models.Model):
	stu_id = models.TextField()
	stu_name = models.TextField()
	num_otp = models.TextField()

class student_marks(models.Model):
	stu_id = models.TextField()
	stu_name = models.TextField()
	test_num = models.TextField(blank=True)
	telugu = models.TextField(blank=True,default='abs')
	maths = models.TextField(blank=True,)
	english = models.TextField(blank=True,)
	hindi = models.TextField(blank=True,)
	physic = models.TextField(blank=True,)
	biology = models.TextField(blank=True,)
	social = models.TextField(blank=True,)
	sanskrit = models.TextField(blank=True,)
	total = models.TextField(blank=True)
	percent = models.TextField(blank=True)
	t_p=models.TextField(blank=True)
	ta = models.TextField(blank=True)
	ma = models.TextField(blank=True)
	ea = models.TextField(blank=True)
	ha = models.TextField(blank=True)
	pa = models.TextField(blank=True)
	ba = models.TextField(blank=True)
	sa = models.TextField(blank=True)
	sana = models.TextField(blank=True)
