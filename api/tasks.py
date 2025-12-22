from celery import shared_task
from .models import SubStudent
from django.utils import timezone
import random



@shared_task
def add_dummy_student():
    # Create a dummy student
    SubStudent.objects.create(
        title=f"Student {random.randint(1,1000)}",
        sub_id=1,  # Replace with valid foreign key if required
        created_at=timezone.now()
    )
    print("Dummy student added")
