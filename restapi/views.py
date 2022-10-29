from django.shortcuts import render
from django.http import JsonResponse
from .models import student
from .serializers import studentSerializer 
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response 

# Create your views here.
@api_view(['GET'])
def student_list(request):
    
    if request.method == 'GET':
        students = student.objects.all()
        serializer = studentSerializer(students, many=True)
        return Response(serializer.data[0])

