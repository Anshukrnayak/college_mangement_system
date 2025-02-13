from django import forms
from .models import StudentModel,CourseModel
from django.contrib.auth.models import User

class StudentRegistrationForm(forms.ModelForm):
    class Meta:
        model = StudentModel
        fields = ['first_name', 'last_name', 'contact', 'email', 'qualification', 'address', 'course']

    first_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'block w-full mt-2 p-3 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500'}))
    last_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'block w-full mt-2 p-3 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500'}))
    contact = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'block w-full mt-2 p-3 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'block w-full mt-2 p-3 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500'}))
    qualification = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'block w-full mt-2 p-3 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500'}))
    address = forms.CharField(widget=forms.Textarea(attrs={'class': 'block w-full mt-2 p-3 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500'}))

