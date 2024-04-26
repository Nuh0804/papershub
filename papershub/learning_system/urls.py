from rest_framework import routers
from .views import *


router = routers.DefaultRouter()
router.register('Course', CourseViewset, basename='course')
router.register('pastpaper', PastpaperViewset, basename='pastpaper')
router.register('tutorial', TutorialViewset, basename='tutorial')
router.register("program", DegreeViewset, basename="degree")

urlpatterns = router.urls 

