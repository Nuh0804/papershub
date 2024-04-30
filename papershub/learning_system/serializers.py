from rest_framework import serializers
from .models import *



class DegreeProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = DegreeProgram
        fields = '__all__'



class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'name',"degree", 'description', 'notes', "year", "semester"]




class TutorialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tutorial
        fields = ['id', 'title', 'course_id', 'file']


class PastPaperSerializer(serializers.ModelSerializer):
    class Meta:
        model = PastPaper
        fields = ['id', 'title', 'course', 'file', 'solution']