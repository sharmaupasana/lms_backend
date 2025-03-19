from django.urls import path
from app.views import addDepartment, deleteDepartment, department


urlpatterns = [
    path('department/', department, name='department'),
    path('delete-department/<str:givenId>', deleteDepartment, name='deleteDeparment'),
    path('add-department', addDepartment, name='addDepartment')
]