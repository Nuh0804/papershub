from rest_framework import routers
from rest_framework_nested.routers import NestedDefaultRouter
from .views import *
from django.urls import path

router = routers.DefaultRouter()
router.register('Course', CourseViewset, basename='course')

lecturerouter = NestedDefaultRouter(router, 'Course', lookup = 'course')
lecturerouter.register('lecture', LectureViewset, basename='lecture')

tutorialrouter = NestedDefaultRouter(router, 'Course', lookup = 'course')
tutorialrouter.register('tutorial', TutorialViewset, basename='tutorial')

papersrouter = NestedDefaultRouter(router, 'Course', lookup = 'course')
papersrouter.register('pastpaper', PastpaperViewset, basename='pastpaper')

urlpatterns = router.urls + lecturerouter.urls + tutorialrouter.urls + papersrouter.urls
