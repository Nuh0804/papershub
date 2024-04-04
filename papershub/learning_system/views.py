from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .serializers import *
from .models import *
from .permissions import IsAdminOrReadOnly

# Create your views here.
class DegreeViewset(ModelViewSet):
    
    queryset = DegreeProgram.objects.all()
    serializer_class = DegreeProgramSerializer

class CourseViewset(ModelViewSet):
    permission_classes = [IsAdminOrReadOnly, IsAuthenticated]
    queryset = Course.objects.all()
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