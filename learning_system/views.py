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
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly]
    def get_queryset(self):
        user = self.request.user
        
        if user.is_superuser:
            return Course.objects.all()
        return Course.objects.filter(degree_id = user.degree_program_id, year = user.year)
    
    serializer_class = CourseSerializer




class PastpaperViewset(ModelViewSet):
    permission_classes = [IsAdminOrReadOnly, IsAuthenticated]
    serializer_class = PastPaperSerializer
    def get_queryset(self):
        course_id = self.kwargs['course_pk']
        return PastPaper.objects.filter(course_id = course_id)