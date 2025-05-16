from django.shortcuts import render, get_object_or_404,get_list_or_404, redirect
from .models import Student, Faculty, Course
from .forms import StudentForm,FacultyForm,CourseForm


# Student management

def home_view(request):
    students = Student.objects.all()
    return render(request, 'home/home.html', {'students': students})

def student_view(request):
    students = Student.objects.all()
    return render(request, 'home/students.html', {'students': students})

def student_register_view(request):
    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(data=request.POST)
        if form.is_valid():
            student = form.save(commit=False)
            try:
                student.faculty = get_object_or_404(Faculty, user=request.user)
                student.save()
                return redirect('students')
            except:
                form.add_error(None, "Faculty not found for this user.")
                return render(request, 'home/register-student.html', {'form': form})
    return render(request, 'home/register-student.html', {'form': form})

def student_update_view(request, pk):
    instance = get_object_or_404(Student, pk=pk)
    form = StudentForm(instance=instance)
    if request.method == 'POST':
        form = StudentForm(data=request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('students')
    return render(request, 'home/register-student.html', {'form': form})

def student_delete_view(request, pk):
    student = get_object_or_404(Student, pk=pk)
    student.delete()
    return redirect('students')


# Manage profile

def faculyt_list_view(request):
   faculties=get_list_or_404(Faculty)
   return render(request,'home/faculty.html',{'faculties':faculties})

def faculty_profile_view(request):
   faculty=get_object_or_404(Faculty,user=request.user)
   return render(request,'home/profile.html',{'faculty':faculty})

def register_faculty_view(request):

   if request.method=='POST':
      form=FacultyForm(data=request.POST,files=request.FILES)
      if form.is_valid():
         faculty=form.save()
         faculty.user=request.user
         faculty.save()
         return redirect('profile')

   return render(request,'home/register-faculty.html',{'form':form})


def faculty_update_view(request,*args,**kwargs):
   form=FacultyForm(instance=get_object_or_404(Faculty,user=request.user))

   if request.method=='POST':
      form = FacultyForm(
         instance=get_object_or_404(Faculty, pk=kwargs['pk']),
         data=request.POST,
         files=request.FILES
      )

      if form.is_valid():
         form.save()
         return redirect('profile')
      print(form.errors)

   return render(request,'home/register-faculty.html',{'form':form})

def faculty_delete_view(request,*args,**kwargs):
   faculty=get_object_or_404(Faculty,user=request.user)
   faculty.delete()

   return redirect('profile')


# course management :
def list_course_view(request):
   courses=Course.objects.all()
   return render(request,'home/course.html',{'courses':courses})

def register_course_view(request):
   form=CourseForm(data=request.POST)
   if form.is_valid():
      form.save()
      return redirect('courses')
   return render(request,'home/register-course.html',{'form':form})


def update_course_view(request,*args,**kwargs):
   instance=get_object_or_404(Course,id=kwargs['pk'])
   form=CourseForm(instance=instance,data=request.POST)
   if form.is_valid():
      form.save()
      return redirect('courses')
   return render(request,'home/register-course.html',{'form':form})


def delete_course_view(request,*args,**kwargs):
   instance=get_object_or_404(Course,pk=kwargs['pk'])
   instance.delete()
   return redirect('courses')


# next day I will implement APIs and authentication
