from rest_framework import serializers
from .models import Employee

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

        def validate_email(self, value):
            if Employee.objects.filter(email=value).exists():
                raise serializers.ValidationError("An employee with this email already exists.")
        
            return value
        
class LoginSerializer(serializers.Serializer):
    username=serializers.CharField()
    password=serializers.CharField()
