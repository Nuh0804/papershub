from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from .models import *
from .permissions import IsAdminOrReadOnly

# Create your views here.
class DegreeViewset(ModelViewSet):
    queryset = DegreeProgram.objects.all()
    serializer_class = DegreeProgramSerializer


class CourseViewset(ModelViewSet):
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly]
    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return Course.objects.all()
        return Course.objects.filter(degree_id = user.degree_program_id, year = user.year)
    
    serializer_class = CourseSerializer




class TutorialViewset(ModelViewSet):
    permission_classes = [IsAdminOrReadOnly, IsAuthenticated]
    queryset = Tutorial.objects.all()
    serializer_class = TutorialSerializer



class PastpaperViewset(ModelViewSet):
    permission_classes = [IsAdminOrReadOnly, IsAuthenticated]
    serializer_class = PastPaperSerializer
    def get_queryset(self):
        course_id = self.kwargs['course_pk']
        user = self.request.user
        course = Course.objects.filter(degree_id = user.degree_program_id, year = user.year)
        if course == course_id:
            return PastPaper.objects.filter(course_id = course_id)
        else:
            return None
