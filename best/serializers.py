from models import *
from rest_framework import serializers

class StudentSerializer(serializers.ModelSerializer):
  class Meta:
    model = Student
    fields = ('id', 'first_name', 'last_name', 'osis_number')

class GroupStudentSerializer(serializers.ModelSerializer):
  student = StudentSerializer()

  class Meta:
    model = GroupStudent
    fields = ('id', 'student', 'date_entered', 'date_left')
    
class GroupSerializer(serializers.ModelSerializer):
  group_students = GroupStudentSerializer(many=True)

  class Meta:
    model = Group
    fields = ('id', 'code', 'group_students')  

