
from django.urls import path
from . import views

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

# urlpatterns = [
#     path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
#     path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),


#     path('register', views.RegisterUserGet.as_view({'get': 'list'}), name= 'registeruser'),
#     path('res/', views.RegisterUserPost.as_view(), name= 'res'),
#     # path('login', views.LoginView.as_view(), name= 'login'),
# ]