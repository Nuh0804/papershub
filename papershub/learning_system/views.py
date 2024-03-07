from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from .models import *
from .permissions import IsAdminOrReadOnly

# Create your views here.

class CourseViewset(ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class LectureViewset(ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    queryset = Lecture.objects.all()
    serializer_class = LectureSerializer


class TutorialViewset(ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    queryset = Tutorial.objects.all()
    serializer_class = TutorialSerializer


class PastpaperViewset(ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    queryset = PastPaper.objects.all()
    serializer_class = PastPaperSerializer