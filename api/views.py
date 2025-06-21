
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from core.models import Student,Faculty,Course
from .serializers import CourseSerializer,StudentSerializer,FacultySerializer


class CourseApiView(APIView):
   permission_classes = [permissions.IsAuthenticatedOrReadOnly,permissions.IsAdminUser]

   def get(self,request):
      instance=Course.objects.all()
      serializer=CourseSerializer(instance=instance,many=True)
      return Response(serializer.data,status=status.HTTP_200_OK)

   def post(self,request):
      data=request.data
      serializers=CourseSerializer(data=data)
      if serializers.is_valid():
         serializers.save()
         return Response(serializers.data,status=status.HTTP_201_CREATED)

class CourseDetailView(APIView):
   permission_classes = [permissions.IsAuthenticated,permissions.IsAdminUser]

   def get_object(self,pk):
      try:
         return Course.objects.get(id=pk)
      except Course.DoesNotExist:
         return None

   def get(self,request,*args,**kwargs):
      instance=self.get_object(kwargs['pk'])
      if instance is not None:
         serializer=CourseSerializer(instance=instance)
         return Response(serializer.data,status=status.HTTP_200_OK)

      return Response(status=status.HTTP_404_NOT_FOUND)

   def put(self,request,*args,**kwargs):
      instance=self.get_object(kwargs['pk'])
      if instance is not None:
         serializer=CourseSerializer(instance=instance,data=request.data)
         if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
      return Response(status=status.HTTP_404_NOT_FOUND)


   def delete(self,request,*args,**kwargs):
      instance=self.get_object(kwargs['pk'])
      instance.delete()
      return Response(status=status.HTTP_204_NO_CONTENT)


class FacultyView(APIView):
   permission_classes = [permissions.IsAuthenticated]

   def get(self,request):
      instance=Faculty.objects.all()
      serializer=FacultySerializer(instance=instance,many=True)
      return Response(serializer.data,status=status.HTTP_200_OK)

   def post(self,request):
      serializer=FacultySerializer(data=request.data)
      if serializer.is_valid():
         serializer.save(user=self.request.user)
         return Response(serializer.data)
      return Response(status=status.HTTP_200_OK)

class FacultyDetailView(APIView):
   permission_classes = [permissions.IsAuthenticated]

   def get_object(self,pk):
      try:
         return Faculty.objects.get(id=pk)
      except Faculty.DoesNotExist:
         return None

   def get(self,request,*args,**kwargs):
      instance=self.get_object(kwargs['pk'])
      if instance is not None:
         serializer=FacultySerializer(instance=instance)
         return Response(serializer.data,status=status.HTTP_200_OK)

      return Response(status=status.HTTP_404_NOT_FOUND)

   def put(self,request,*args,**kwargs):
      instance=self.get_object(kwargs['pk'])
      if instance is not None:
         serializer=FacultySerializer(instance=instance,data=request.data)
         if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

      return Response(status=status.HTTP_404_NOT_FOUND)

   def delete(self,request,*args,**kwargs):
      instance=self.get_object(kwargs['pk'])
      instance.delete()

      return Response(status=status.HTTP_200_OK)

class StudentView(APIView):
   permission_classes = [permissions.IsAuthenticated]

   def get(self,request):
      instance=Student.objects.all()
      serializer=StudentSerializer(instance=instance,many=True)
      return Response(serializer.data,status=status.HTTP_200_OK)

   def post(self,request):
      try:
         faculty=Faculty.objects.get(user=request.user)

         serializer=StudentSerializer(data=request.data)
         if serializer.is_valid():
            serializer.save(faculty=faculty)

            return Response(serializer.data,status=status.HTTP_200_OK)

         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

      except Faculty.DoesNotExist:
         return Response(status=status.HTTP_400_BAD_REQUEST)

class StudentDetailView(APIView):
   permission_classes = [permissions.IsAuthenticated]

   def get_object(self,pk):
      try:
         return Student.objects.get(id=pk)
      except Student.DoesNotExist:
         return None

   def get(self,request,*arge,**kwargs):
      instance=self.get_object(kwargs['pk'])
      if instance is not None:
         serializer=StudentSerializer(instance=instance)
         return Response(serializer.data,status=status.HTTP_200_OK)
      return Response(status=status.HTTP_404_NOT_FOUND)

   def put(self,request,*args,**kwargs):
      instance=self.get_object(kwargs['pk'])
      if instance is not None:
         serializer=StudentSerializer(instance=instance,data=request.data)
         if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

      return Response(status=status.HTTP_404_NOT_FOUND)

# updating some part of code for check