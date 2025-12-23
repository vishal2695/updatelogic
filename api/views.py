from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from .models import Student, SubStudent
from .serializers import StudentSerializer

from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import AccessToken, UntypedToken



####  >>>>>>>>>>>>>>>>.
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import MyTokenObtainPairSerializer
from jwt.exceptions import InvalidTokenError
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

import jwt
from django.conf import settings
from datetime import datetime




@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_students(request):
    auth = request.headers.get("Authorization")

    token_str = auth.split(" ")[1]          # extract token
    access_token = AccessToken(token_str)   # decode
    payload = access_token.payload      # convert to dict


    students = Student.objects.all()
    serializer = StudentSerializer(students, many=True)
    return Response({"data":serializer.data, "token_data":payload})


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_student(request):
    serializer = StudentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_test(request):
    auth = request.headers.get("Authorization")

    token_str = auth.split(" ")[1]          # extract token
    access_token = AccessToken(token_str)   # decode
    payload = access_token.payload      # convert to dict

    timestamp = payload["exp"]
    dt_utc = datetime.utcfromtimestamp(timestamp)
    print(dt_utc)
    payload["expiry_time"] = dt_utc
    from django.utils import timezone

    current_utc_time = timezone.now()
    print(current_utc_time)

    payload["current_time"] = current_utc_time


    ss = SubStudent.objects.select_related('sub')
    print(ss)
    jj = SubStudent.objects.select_related('sub').filter(sub__email="vishal@gmail.com")
    print(jj)
    kk = SubStudent.objects.select_related('sub').values(
    'title',
    'sub__name',
    'sub__email'
    )
    print(kk)
    ll = SubStudent.objects.select_related('sub').only(
    'title',
    'sub__email'
    )
    print(ll)
    for l in ll:
        gg = l.sub.name if l.sub else None
        print(gg)
    students = Student.objects.all()
    serializer = StudentSerializer(students, many=True)
    return Response({"data":serializer.data, "token_data":payload})



from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1 style='text-align:center;'>Welcome to the Smart World!@!</h1>")


