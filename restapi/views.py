from django.shortcuts import render
from django.http import JsonResponse
from .models import Input
from .serializers import InputSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response 

# Create your views here.
@api_view(['POST', 'GET'])

#def student_list(request):
    #if request.method == 'GET':
        #students = student.objects.all()
        #serializer = studentSerializer(students, many=True)
        #return Response(serializer.data[0])

def test3(request):
    serializer = InputSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save() 

    operation = Input.objects.all()
    serializer = InputSerializer(operation, many=True)
    choice = serializer.data[-1]["operation_type"]  
   

    def res():
        num1 = serializer.data[-1]["x"]
        num2 = serializer.data[-1]["y"] 

        add = num1 + num2
        sub = num1 - num2
        mul = num1 * num2 

        if choice == "addition":
            result = add
        elif choice == "subtraction":
            result = sub
        elif choice == "multiplication":
            result = mul

        return result 

     

    #def finalanswer():
        #answer = ({"slackUsername": "muobotone", "result": anser, "operation_type" : choice})

        #return answer


    #return Response(answer)

    answer = res()
    return Response({"slackUsername": "Oiseh", "result": answer, "operation_type" : choice}) 

