from django.shortcuts import render,redirect,get_object_or_404
from django.views import generic,View
from django.contrib.auth.models import User
from .models import CourseModel,FacultyModel,StudentModel
from .forms import StudentRegistrationForm
from django.contrib.auth.mixins import  LoginRequiredMixin

# Course
class CourseListView(LoginRequiredMixin,generic.ListView):
    template_name = 'home/index.html'
    model = CourseModel
    context_object_name = 'course_list'


class CourseDetailView(LoginRequiredMixin,generic.DetailView):
    template_name = 'home/detail.html'
    model=CourseModel
    context_object_name = 'course'


# Here student can register to the course
class RegisterStudentView(LoginRequiredMixin,View):
    def get(self,request):
        form=StudentRegistrationForm
        return render(request,'home/registration.html',{'form':form})

    def post(self,request):
        form=StudentRegistrationForm(data=request.POST)
        if form.is_valid():
            student=form.save(commit=False)
            student.user=self.request.user
            student.save()

            return redirect('home')

        return render(request,'home/registration.html',{'form':form})

# User can see his/her profile  :
class ProfileView(LoginRequiredMixin,View):
    def get(self,request):
            profile=get_object_or_404(FacultyModel,user=request.user)
            print(profile)
            return render(request,'home/profile.html',{'profile':profile})

# List of Students who are enrolled in course.
class StudentView(LoginRequiredMixin,generic.ListView):
    template_name = 'home/student.html'
    model = StudentModel
    context_object_name = 'student_list'



