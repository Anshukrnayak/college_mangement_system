from django.shortcuts import render
from django.views import generic,View
from django.contrib.auth.models import User
from .models import CourseModel

# Course
class CourseListView(generic.ListView):
    template_name = 'home/index.html'
    model = CourseModel
    context_object_name = 'course_list'


class CourseDetailView(generic.DetailView):
    template_name = 'home/detail.html'
    model=CourseModel
    context_object_name = 'course'



