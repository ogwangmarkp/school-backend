from rest_framework import serializers
from .models import *

class StaffSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    date_added = serializers.DateTimeField(read_only=True)
    added_by = serializers.IntegerField(read_only=True)

    class Meta:
        model = Staff
        fields = '__all__' 