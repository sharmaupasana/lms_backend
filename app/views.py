from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from app.models import Course, Department, Semester, Student
from app.serializers import (CourseSerializer, DepartmentSerializer, SemesterSerializer,
    StudentSerializer)

# Departments.
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

@api_view(['POST'])
def editDepartment(request):
    datas = request.data
    department = Department.objects.get(id=datas['departmentId'])
    department.name = datas['departmentName']
    department.save()
    return Response({'status': 200})




# Semester
@api_view(['GET'])
def semester(request):
    data = {
        'semesters': SemesterSerializer(Semester.objects.all(), many=True).data
    }
    return Response(data)

@api_view(['GET'])
def deleteSemester(request, givenId):
    Semester.objects.get(id=givenId).delete()
    return Response({'status': 200})

@api_view(['POST'])
def addSemester(request):
    datas = request.data
    Semester(name=datas['name'], symbol=datas['symbol']).save()
    return Response({'status': 200})

@api_view(['POST'])
def editSemester(request):
    datas = request.data
    semester = Semester.objects.get(id=datas['id'])
    semester.name = datas['name']
    semester.symbol = datas['symbol']
    semester.save()
    return Response({'status': 200})




# Course
@api_view(['GET'])
def course(request):
    data = {
        'departments': DepartmentSerializer(Department.objects.all(), many=True).data,
        'semesters': SemesterSerializer(Semester.objects.all(), many=True).data,
        'courses': CourseSerializer(Course.objects.all(), many=True).data
    }
    return Response(data)

@api_view(['POST'])
def addCourse(request):
    datas = request.data
    department = Department.objects.get(id = datas['department'])
    semesters = Semester.objects.filter(id__in=datas['semesters'])
    course = Course(name=datas['name'], department=department)
    course.save()
    course.semesters.set(semesters)
    return Response({'status': 200})

@api_view(['GET'])
def deleteCourse(request, id):
    Course.objects.get(id=id).delete()
    return Response({'status': 200})