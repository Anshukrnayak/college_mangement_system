from django.shortcuts import render, get_object_or_404, redirect
from .models import Student, Faculty, Course
from .forms import StudentForm,FacultyForm

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
def faculty_profile_view(request):
   faculty=get_object_or_404(Faculty,user=request.user)
   return render(request,'home/profile.html',{'faculty':faculty})


def faculty_update_view(request,*args,**kwargs):
   form=FacultyForm(instance=get_object_or_404(Faculty,user=request.user))

   if request.method=='POST':
      form=FacultyForm(instance=get_object_or_404(Faculty,user=request.user))
      if form.is_valid():
         form.save()

         return redirect('')


def faculty_delete_view(request,*args,**kwargs):
   pass

# I will complete this next day :



