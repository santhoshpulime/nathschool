from django.contrib import admin
from .models import classroom,student,opt,student_marks
admin.site.register(classroom)
admin.site.register(student)
admin.site.register(opt)
admin.site.register(student_marks)