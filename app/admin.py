from django.contrib import admin
from app.models import Book, Course, Department, Semester, Student

# Register your models here.
@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['name']
    

@admin.register(Semester)
class SemesterAdmin(admin.ModelAdmin):
    list_display = ['name', 'symbol']


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['name', 'department']


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['name', 'code', 'course', 'semester', 'edition']


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['name', 'symbol', 'department', 'course', 'semester']
    