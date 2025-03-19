from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from app.models import Course, Department, Student
from app.serializers import CourseSerializer, DepartmentSerializer, StudentSerializer

# Create your views here.
@api_view(['GET'])
def department(request):
    data = {
        'departments': DepartmentSerializer(Department.objects.all(), many=True).data
    }
    return Response(data)


@api_view(['GET'])
def deleteDepartment(request, givenId):
    Department.objects.get(id=givenId).delete()
    return Response({'status': 200})

@api_view(['POST'])
def addDepartment(request):
    datas = request.data
    Department(name=datas['departmentName']).save()
    return Response({'status': 200})