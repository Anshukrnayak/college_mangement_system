from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Course(BaseModel):
    name = models.CharField(max_length=50)
    duration = models.IntegerField()
    fees = models.PositiveIntegerField(default=40000)

    def clean(self):
        if self.fees < 0:
            raise ValidationError('Fees must be a positive number.')

    def __str__(self):
        return self.name


class Faculty(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='faculty',default=True)
    profile_pic = models.ImageField(upload_to='media/profile_pic', blank=True, null=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    experience = models.PositiveIntegerField(default=1, validators=[MinValueValidator(0)])
    salary = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(10000)])
    course = models.ManyToManyField(Course, related_name='faculty')

    def clean(self):
        if self.experience is not None and self.experience < 0:
            raise ValidationError({'experience': 'Experience cannot be negative.'})

        if self.salary is not None and self.salary < 0:
            raise ValidationError({'salary': 'Salary cannot be negative.'})



    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Student(BaseModel):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    location = models.CharField(max_length=250)
    faculty = models.ForeignKey(Faculty, on_delete=models.SET_NULL, null=True, blank=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='students')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
