from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from myusers.models import User
from .serializers import *
from .models import *
from .permissions import IsAdminOrReadOnly

# Create your views here.
class DegreeViewset(ModelViewSet):
    
    queryset = DegreeProgram.objects.all()
    serializer_class = DegreeProgramSerializer

class CourseViewset(ModelViewSet):
    permission_classes = [IsAdminOrReadOnly, IsAuthenticated]
    def get_queryset(self):
        user = self.request.user
        profile = User.objects.filter(id = user.id).first()
        return Course.objects.filter(degree_id_id = profile.degree_program, year_taught = profile.year)
    serializer_class = CourseSerializer



class LectureViewset(ModelViewSet):
    permission_classes = [IsAdminOrReadOnly, IsAuthenticated]
    queryset = Lecture.objects.all()
    serializer_class = LectureSerializer


class TutorialViewset(ModelViewSet):
    permission_classes = [IsAdminOrReadOnly, IsAuthenticated]
    queryset = Tutorial.objects.all()
    serializer_class = TutorialSerializer


class PastpaperViewset(ModelViewSet):
    permission_classes = [IsAdminOrReadOnly, IsAuthenticated]
    queryset = PastPaper.objects.all()
    serializer_class = PastPaperSerializer