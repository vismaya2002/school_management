from rest_framework import serializers
from .models import StudentDetails 

class StudentDetailserializer(serializers.ModelSerializer):
    class Meta:
        model = StudentDetails
        fields = ['student_id','name','grade','section','rollnumber']