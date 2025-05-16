from core.models import Student,Faculty,Course
from rest_framework import serializers


class CourseSerializer(serializers.ModelSerializer):
   class Meta:
      model=Course
      fields='__all__'


class StudentSerializer(serializers.ModelSerializer):
   class Meta:
      model=Student
      fields='__all__'


class FacultySerializer(serializers.ModelSerializer):
   students=StudentSerializer(many=True,read_only=True)

   class Meta:
      model=Faculty
      fields=['first_name','last_name','salary','course','students']

