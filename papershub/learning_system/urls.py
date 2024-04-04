from rest_framework import routers
from rest_framework_nested.routers import NestedDefaultRouter
from .views import *
from django.urls import path, include

router = routers.DefaultRouter()
router.register('Course', CourseViewset, basename='course')

degreerouter = routers.DefaultRouter()
degreerouter.register("program", DegreeViewset, basename="degree")

lecturerouter = NestedDefaultRouter(router, 'Course', lookup = 'course')
lecturerouter.register('lecture', LectureViewset, basename='lecture')

tutorialrouter = NestedDefaultRouter(router, 'Course', lookup = 'course')
tutorialrouter.register('tutorial', TutorialViewset, basename='tutorial')

papersrouter = NestedDefaultRouter(router, 'Course', lookup = 'course')
papersrouter.register('pastpaper', PastpaperViewset, basename='pastpaper')

# userprofilerouter = routers.DefaultRouter()
# router.register('profile', UserProfileView, basename='profile')



urlpatterns = router.urls + lecturerouter.urls + tutorialrouter.urls + papersrouter.urls + degreerouter.urls
