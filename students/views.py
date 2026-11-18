from django.shortcuts import render,get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from .permissions import IsStudentOrReadOnly


class StudentListCreate(APIView):
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsStudentOrReadOnly]

    def get(self,request):
        s=Student.objects.all()
        serializer=StudentSerializer(s,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def post(self,request):
        serializer=StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class RetreiveUpdateDelete(APIView):

    authentication_classes=[TokenAuthentication]
    permission_classes=[IsStudentOrReadOnly]

    def get(self,request,id):
        s=get_object_or_404(Student,id=id)
        serializer=StudentSerializer(s)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def put(self,request,id):
        s=get_object_or_404(Student,id=id)
        serializer=StudentSerializer(s,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def patch(self,request,id):
        s=get_object_or_404(Student,id=id)
        serializer=StudentSerializer(s,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,id):
        s=get_object_or_404(Student,id=id)
        s.delete()
        return Response({"message":"Student Record Deleted"})





# 628cf5f6804e962281279a057e7b99ca6a55095b
# 7b2b8ca6f4febbdb5a559439e525df5d1dc3a46f