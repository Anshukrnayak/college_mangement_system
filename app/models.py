from django.db import models
from django.contrib.auth.models import  User
# Create your models here.

class BaseModel(models.Model):
    created_at=models.DateField(auto_now=True)
    updated_at=models.DateField(auto_now_add=True)

    class Meta:
        abstract=True

class DepartmentModel(BaseModel):
    name=models.CharField(max_length=50)
    def __str__(self): return self.name

class CourseModel(BaseModel):
    name=models.CharField(max_length=50)
    duration=models.IntegerField(default=3)
    fees=models.IntegerField(default=5000)

    def __str__(self): return self.name


class FacultyModel(BaseModel):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='faculty')
    course=models.ManyToManyField(CourseModel)
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    contact=models.CharField(max_length=50)
    location=models.TextField()
    experience=models.IntegerField(default=2)
    is_faculty=models.BooleanField(default=True)

    def __str__(self): return f' {self.first_name} {self.last_name} '


class StudentModel(BaseModel):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='student')
    course=models.ForeignKey(CourseModel, on_delete=models.CASCADE ,related_name='student')
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    contact=models.IntegerField()
    email=models.EmailField()
    qualification=models.CharField(max_length=100)
    address=models.TextField()

    def __str__(self): return f' {self.first_name} {self.last_name} '


