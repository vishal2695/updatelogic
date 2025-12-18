from django.db import models

# Create your models here.



class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

class SubStudent(models.Model):
    sub   = models.ForeignKey(Student, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=100)
    address = models.TextField()