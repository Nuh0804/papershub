from rest_framework import routers
from django.urls import path, include
from rest_framework_nested.routers import NestedDefaultRouter
from .views import *


router = routers.DefaultRouter()
router.register('Course', CourseViewset, basename="Course")
router.register("program", DegreeViewset, basename="degree")

paperrouter = NestedDefaultRouter(router, "Course", lookup = 'course')
paperrouter.register("paper", PastpaperViewset, basename='paper')

urlpatterns = router.urls + paperrouter.urls 