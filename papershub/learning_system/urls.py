from rest_framework import routers
from rest_framework_nested.routers import NestedDefaultRouter
from .views import *


router = routers.DefaultRouter()
router.register('Course', CourseViewset, basename='course')
router.register('tutorial', TutorialViewset, basename='tutorial')
router.register("program", DegreeViewset, basename="degree")

paperrouter = NestedDefaultRouter(router, "Course", lookup = 'course')
paperrouter.register("paper", PastpaperViewset, basename='paper')
urlpatterns = router.urls + paperrouter.urls

