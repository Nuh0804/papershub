from rest_framework import serializers
from .models import User
from djoser.serializers import UserCreateSerializer, UserSerializer, TokenCreateSerializer, TokenSerializer


class RegisterUserSerializer(serializers.ModelSerializer):
   class Meta:
      model = User
      fields = [
         'id',
         'first_name',
         'last_name',
         'email',
         'phone_number',
         'password',
      ]
   
      def create(self, validated_data):
         password = validated_data.pop('password', None)
         instance = self.Meta.model(**validated_data)
         if password is not None:
            instance.set_password(password)
         instance.save()
         return instance
   

class UserCreaterSerializer(UserCreateSerializer):
   class Meta(UserCreateSerializer.Meta):
      fields = ['id', 'username', 'password', 'email', 'first_name', 'last_name', 'phone_number']

class CurrentUserSerializer(UserSerializer):
   class Meta(UserSerializer.Meta):
      fields = ['email', 'id','first_name', 'last_name']
      