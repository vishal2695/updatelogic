from celery import shared_task
from .models import SubStudent, Student
from django.utils import timezone
import random



@shared_task
def add_dummy_student():
    # Create a dummy student
    SubStudent.objects.create(
        title=f"Student {random.randint(1,1000)}",
        sub_id=1
    )
    print("Dummy child student added")


@shared_task
def addd_dummy_student():
    # Create a dummy student
    Student.objects.create(
        name=f"Student {random.randint(1,1000)}",
        email=f"Student{random.randint(1,1000)}@gmail.com",
    )
    print("Dummy student addedd")
