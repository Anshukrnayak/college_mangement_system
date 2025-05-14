from django.urls import path
from . import views

urlpatterns=[

   path('',views.home_view,name='home'),
   path('student/',views.student_view,name='students'),
   path('student-register/',views.student_register_view,name='student-register'),
   path('student-delete/<int:pk>/',views.student_delete_view,name='student-delete'),
   path('student-update/<int:pk>/',views.student_update_view,name='student-update'),

   # faculty
   path('profile/',views.faculty_profile_view,name='profile'),
   path('faculty-update/<int:pk>/',views.faculty_update_view,name='faculty_update'),


]