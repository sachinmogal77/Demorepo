
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Student
from .serializers import StudentSerializers



class StudentApi(APIView):
    def get(self,request):
        students = Student.objects.all()
        serializer = StudentSerializers(students,many=True)
        return Response(data=serializer.data,status=status.HTTP_200_OK)

    def post(self,request):
        serializer  = StudentSerializers(data=request.data,)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data,status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class StudentDetailsApi(APIView):
    def get(self,request,pk):
        try:
            student = Student.objects.get(pk=pk)
            serializer = StudentSerializers(student)
            return Response(data=serializer.data,status=status.HTTP_200_OK)
        except Student.DoesNotExist:
            data={"msg":"The record You're looking does not exist"}
            return Response(data=data,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk):
        try:
            student = Student.objects.get(pk=pk)
            student.delete()
            return Response(data={"msg":"No Content"},status=status.HTTP_204_NO_CONTENT)
        except Student.DoesNotExist:
             data={"msg":"The record You're looking does not exist"}
             return Response(data=data,status=status.HTTP_400_BAD_REQUEST)

    def put(self,request,pk):
        try:
            student = Student.objects.get(pk=pk)
            serializer = StudentSerializers(data=request.data,instance=student,partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(data=serializer.data,status=status.HTTP_205_RESET_CONTENT)
            return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        except Student.DoesNotExist:
             data={"msg":"The record You're looking does not exist"}
             return Response(data=data,status=status.HTTP_404_NOT_FOUND)


            
        



