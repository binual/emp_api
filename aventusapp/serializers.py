from rest_framework import serializers
from aventusapp.models import *

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Employee
        fields = '__all__'
        