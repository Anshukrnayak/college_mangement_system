from django.test import TestCase
from django.core.exceptions import ValidationError
from .models import Faculty, Course, Student
from django.contrib.auth.models import User

class TestCollegeManage(TestCase):

    def setUp(self):
        # Create a user with a hashed password using create_user
        self.user = User.objects.create_user(username='abhijeet', password='#include')

        # Create a course
        self.course = Course.objects.create(name='BCA', duration=3, fees=50000)

        # Create a faculty member and assign the course to them
        self.faculty = Faculty.objects.create(
            user=self.user,
            first_name='Abhijeet',
            last_name='Kumar',
            salary=9000,
            experience=2
        )
        self.faculty.course.add(self.course)  # Add the course after the faculty instance is created

        # Create a student and assign the faculty and course
        self.student = Student.objects.create(
            first_name='Nitish',
            last_name='Kumar',
            location='Hazaribagh',
            faculty=self.faculty,
            course=self.course
        )

    def test_course(self):
        self.course.fees = -1  # Set invalid fees
        with self.assertRaises(ValidationError):  # Expect a validation error
            self.course.clean()  # Call clean() to trigger validation

    def test_faculty(self):
        # Test invalid salary
        self.faculty.salary = 0  # Set invalid salary
        with self.assertRaises(ValidationError):
            self.faculty.clean()  # Expect validation error

        # Test invalid experience
        self.faculty.experience = -1  # Set invalid experience
        with self.assertRaises(ValidationError):
            self.faculty.clean()  # Expect validation error

