from rest_framework import serializers
from .models import *

class YearCHoices(models.IntegerChoices):
    first = 1
    second = 2
    third = 3
    fourth = 4

class DegreeProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = DegreeProgram
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    # degree_id = DegreeProgramSerializer(many = True, read_only = True)
    # year_taught =serializers.ListField(child = serializers.IntegerField(), required = False, allow_empty = True)
    class Meta:
        model = Course
        fields = ['id', 'name', 'description', 'degree_id', 'year_taught', 'semester', 'notes']
        


class TutorialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tutorial
        fields = ['id', 'title', 'course_id', 'file']


class PastPaperSerializer(serializers.ModelSerializer):
    class Meta:
        model = PastPaper
        fields = ['id', 'title', 'course_id', 'file', 'solution']