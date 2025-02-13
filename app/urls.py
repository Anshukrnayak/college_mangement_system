from django.urls import path
from . import views

urlpatterns=[

    path('',views.CourseListView.as_view(),name='home'),
    path('detail/<int:pk>',views.CourseDetailView.as_view(),name='course_detail'),
    path('student-registration/', views.RegisterStudentView.as_view(), name='student_registration'),
    path('profile',views.ProfileView.as_view(),name='profile'),
    path('student',views.StudentView.as_view(),name='student'),



]