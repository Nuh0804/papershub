from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
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
        if user.is_superuser:
            return Course.objects.all()
        profile = User.objects.filter(id = user.id).first()
        return Course.objects.filter(degree_id = profile.degree_program, year_taught = profile.year)
    serializer_class = CourseSerializer




class TutorialViewset(ModelViewSet):
    permission_classes = [IsAdminOrReadOnly, IsAuthenticated]
    queryset = Tutorial.objects.all()
    serializer_class = TutorialSerializer


class PastpaperViewset(ModelViewSet):
    permission_classes = [IsAdminOrReadOnly, IsAuthenticated]
    queryset = PastPaper.objects.all()
    serializer_class = PastPaperSerializer