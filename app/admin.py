from django.contrib import admin
from .models import DepartmentModel,CourseModel,FacultyModel,StudentModel

admin.site.register(DepartmentModel)
admin.site.register(CourseModel)
admin.site.register(FacultyModel)
admin.site.register(StudentModel)



