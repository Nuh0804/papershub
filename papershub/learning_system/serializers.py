from rest_framework import serializers
from .models import *

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'name', 'description']
        

class LectureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lecture
        fields = ['id', 'title', 'course_id', 'file']


class TutorialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tutorial
        fields = ['id', 'title', 'course_id', 'file']


class PastPaperSerializer(serializers.ModelSerializer):
    class Meta:
        model = PastPaper
        fields = ['id', 'title', 'course_id', 'file', 'solution']