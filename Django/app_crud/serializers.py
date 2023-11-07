from rest_framework import serializers
from .models import *


class schoolserializer(serializers.ModelSerializer):
    class Meta:
        model = school
        fields = '__all__'


class studentserializer(serializers.ModelSerializer):
    class Meta:
        model = student
        fields = '__all__'


class teacherserializer(serializers.ModelSerializer):
    class Meta:
        model = teacher
        fields = '__all__'


class courseserializer(serializers.ModelSerializer):
    class Meta:
        model = course
        fields = '__all__'


class busserializer(serializers.ModelSerializer):
    class Meta:
        model = bus
        fields = '__all__'


class Facultyserializer(serializers.ModelSerializer):
    class Meta:
        model = Faculty
        fields = '__all__'
