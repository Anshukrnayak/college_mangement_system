from django.urls import path
from . import views
urlpatterns=[

   path('course/',views.CourseApiView.as_view(),name='course'),
   path('course/<int:pk>/',views.CourseDetailView.as_view(),name='course-detail'),
   path('faculty/',views.FacultyView.as_view(),name='faculty'),
   path('faculty/<int:pk>/',views.FacultyDetailView.as_view(),name='faculty-detail'),
   path('student/',views.StudentView.as_view(),name='student'),
   path('student/<int:pk>/',views.StudentDetailView.as_view(),name='student-detail')


]