
from django.urls import path
from .views import CustomTokenObtainPairView, OrderViewset
from rest_framework_simplejwt import views as jwt_views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('login/', CustomTokenObtainPairView.as_view(), name='login'),
    path('refresh/', jwt_views.TokenRefreshView.as_view(), name='refresh'),
    

]

