from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from aventusapp.models import *
from aventusapp.serializers import EmployeeSerializer
from rest_framework import status


@api_view(['GET','POST','PUT','PATCH','DELETE'])   
def employee(request):
    if request.method == 'GET':
        emp=Employee.objects.all()
        serializer = EmployeeSerializer(emp,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        data=request.data
        serializer = EmployeeSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors)
    elif request.method == 'PUT':
        data = request.data
        obj=Employee.objects.get(id=data['id'])
        serializer = EmployeeSerializer(obj,data=data,partial=False)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    elif request.method == 'PATCH':
        data = request.data
        obj=Employee.objects.get(id=data['id'])
        serializer = EmployeeSerializer(obj,data=data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    elif request.method == 'DELETE':
    
            data = request.data
            obj = Employee.objects.get(id=data['id'])
            obj.delete()
            return Response("Deleted Successfully", status=status.HTTP_204_NO_CONTENT)
        