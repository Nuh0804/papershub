
from django.urls import path
from .views import CustomTokenObtainPairView
from rest_framework_simplejwt import views as jwt_views
# from .views import ActivateUser

urlpatterns = [
    path('login/', CustomTokenObtainPairView.as_view(), name='login'),
    path('refresh/', jwt_views.TokenRefreshView.as_view(), name='refresh'),
    # path('activation/<str:uid>/<str:token>', ActivateUser.as_view({'get': 'activation'}), name='activation'),
]

