from rest_framework import serializers
from .models import *

class StudentSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    date_added = serializers.DateTimeField(read_only=True)
    added_by = serializers.IntegerField(read_only=True)

    class Meta:
        model = Student
        fields = '__all__' 