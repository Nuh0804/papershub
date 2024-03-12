# from django.shortcuts import render
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from rest_framework.viewsets import ModelViewSet,generics
# from .models import User
# from rest_framework.permissions import AllowAny
# from . serializers import RegisterUserSerializer
# from rest_framework import status



# # Create your views here.
# class RegisterUserGet(ModelViewSet):
#     permission_classes = [AllowAny]
#     queryset = User.objects.all()
#     serializer_class = RegisterUserSerializer

# class RegisterUserPost(APIView):
#     permission_classes = [AllowAny]
#     def post(self, request):
#          #queryset = User.objects.get()
#          serializer = RegisterUserSerializer(data= request.data)
#          if serializer.is_valid():
#             serializer.save()
#             message = {'save': True}
#             return Response(message)
#          return Response(status, status= status.HTTP_400_BAD_REQUEST)


# class LoginView(APIView):
    # permission_classes = [AllowAny]
    # def post(self, request):
        # email = request.data.email
        # password = request.data.password

        # user = User.objects.filter(email=email).first()

        # if user is None:
        #     raise AuthenticationFailed('user not found')
        
        # if not user.check_password(password):
        #     raise AuthenticationFailed('incorrect password')
        
        # return Response(user)