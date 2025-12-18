from rest_framework import serializers
from .models import Student



class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'




from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # 🔥 Add custom fields here
        token['email'] = user.email
        token['first_name'] = user.first_name
        token['last_name'] = user.last_name
        token['is_admin'] = user.is_staff
        token['joined'] = str(user.date_joined)
        token['kk'] = "testing"

        
        # Example if you have profile data:
        # token['phone'] = user.profile.phone
        # token['role'] = user.profile.role

        return token