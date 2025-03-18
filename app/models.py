from django.db import models

# Create your models here.
class Department(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name


class Semester(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    symbol = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name
    

class Course(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True)
    semesters = models.ManyToManyField(Semester)
    
    def __str__(self):
        return self.name


class Book(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=255, blank=True, null=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE, null=True)
    edition = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name + " - " + self.edition


class Student(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    symbol = models.CharField(max_length=255, unique=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to='students/', blank=True, null=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return self.name


class StudentBook(models.Model):
    id = models.BigAutoField(primary_key=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='student_books', null=True)
    book = models.ForeignKey(Book, related_name='student_books', on_delete=models.CASCADE, null=True)
    issue_date = models.DateField()
    return_date = models.DateField(blank=True, null=True)
    
    def __str__(self):
        return self.student.name + " - " + self.book.name