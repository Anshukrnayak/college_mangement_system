from django.urls import path
from . import views

urlpatterns=[

   # student management
   path('',views.home_view,name='home'),
   path('student/',views.student_view,name='students'),
   path('student-register/',views.student_register_view,name='student-register'),
   path('student-delete/<int:pk>/',views.student_delete_view,name='student-delete'),
   path('student-update/<int:pk>/',views.student_update_view,name='student-update'),

   # faculty management
   path('profile/',views.faculty_profile_view,name='profile'),
   path('faculty-register/',views.register_faculty_view,name='faculty-register'),
   path('faculty-update/<int:pk>/',views.faculty_update_view,name='faculty_update'),
   path('faculty-delete/<int:pk>/',views.faculty_delete_view,name='faculty-delete')

   # course management


]