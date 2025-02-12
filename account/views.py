from django.shortcuts import render,redirect
from django.contrib.auth.models import  User
from django.views import  View
from .forms import SignupForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin

# Signup page for registration of new user :
class SignupView(View):
    def get(self,request):
        form=SignupForm()
        return render(request,'account/signup.html',{'form':form})

    def post(self,request):
        form=SignupForm()
        if form.is_valid():
            form.save()
            return redirect('home')

# Login page for check user is authenticate
class LoginView(View):
    def get(self,request):
        return render(request,'account/login.html')

    def post(self,request):

        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)

        if user is not None:
            login(request,user)
            messages.info(request,'username login successfully.....')
            return redirect('home')

        messages.error(request,'username or password was not valid please enter correct username or password ')
        return render(request,'account/login.html')



# Logout view :
class LogoutView(LoginRequiredMixin,View):
    def get(self,request):
        logout(request)
        return redirect('home')

