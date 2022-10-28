from django.shortcuts import render
from django.http import JsonResponse
from .models import student
from .serializers import studentSerializer  

# Create your views here.
def student_list(request):
    students = student.objects.all()
    serializer = studentSerializer(students, many=True)
    return JsonResponse(serializer.data, safe=False)

