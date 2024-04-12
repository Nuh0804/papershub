from django.conf import settings
from rest_framework import status
from djoser.views import UserViewSet
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


class CustomTokenObtainPairView(TokenObtainPairView):
    def post(self, request: Request, *args, **kwargs) -> Response:
        response = super().post(request, *args, **kwargs)
        access_token= response.data['access']
        response.set_cookie(
            key=settings.SIMPLE_JWT['AUTH_COOKIE'],
            value=access_token,
            domain=settings.SIMPLE_JWT["AUTH_COOKIE_DOMAIN"],
            path=settings.SIMPLE_JWT["AUTH_COOKIE_PATH"],
            expires=settings.SIMPLE_JWT["ACCESS_TOKEN_LIFETIME"],
            secure=settings.SIMPLE_JWT["AUTH_COOKIE_SECURE"],
            httponly=settings.SIMPLE_JWT["AUTH_COOKIE_HTTP_ONLY"],
            samesite=settings.SIMPLE_JWT["AUTH_COOKIE_SAMESITE"],
        )
        return response



# class ActivateUser(UserViewSet):

#     def get_serializer(self, *args, **kwargs):
#         serializer_class = self.get_serializer_class()
#         kwargs.setdefault('context', self.get_serializer_context())
 
#         kwargs['data'] = {"uid": self.kwargs['uid'], "token": self.kwargs['token']}
 
#         return serializer_class(*args, **kwargs)
 
#     def activation(self, request, uid, token, *args, **kwargs):
#         super().activation(request, *args, **kwargs)
#         return Response(status=status.HTTP_204_NO_CONTENT)
    
