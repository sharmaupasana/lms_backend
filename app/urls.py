from django.urls import path
from app.views import (addCourse, addDepartment, addSemester, course, deleteCourse,
    deleteDepartment, deleteSemester, department, editDepartment, editSemester, semester)


urlpatterns = [
    
    # Departments
    path('department/', department, name='department'),
    path('delete-department/<str:givenId>', deleteDepartment, name='deleteDeparment'),
    path('add-department', addDepartment, name='addDepartment'),
    path('edit-department', editDepartment, name='editDepartment'),
    
    # Semester
    path('semester', semester, name='semester'),
    path('delete-semester/<str:givenId>', deleteSemester, name='deleteSemester'),
    path('add-semester', addSemester, name='addSemester'),
    path('edit-semester', editSemester, name='editSemester'),
    
    # Course
    path('course', course, name='course'),
    path('add-course', addCourse, name='addCourse'),
    path('delete-course/<str:id>', deleteCourse, name='deleteCourse')
]