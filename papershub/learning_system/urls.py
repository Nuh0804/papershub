from rest_framework import routers
from django.urls import path, include
from rest_framework_nested.routers import NestedDefaultRouter
from .views import *


router = routers.DefaultRouter()
router.register('Course', CourseViewset, basename="Course")
router.register('tutorial', TutorialViewset, basename='tutorial')
router.register("program", DegreeViewset, basename="degree")
router.register("paper", PastpaperViewset, basename="paper")

paperrouter = NestedDefaultRouter(router, "Course", lookup = 'course')
paperrouter.register("paper", PastpaperViewset, basename='paper')

urlpatterns = router.urls + paperrouter.urls 