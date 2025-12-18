from django.urls import path
from . import views



urlpatterns = [
    path('students/', views.get_students),
    path('students/add/', views.add_student),
    path('students/test/', views.get_test),


]