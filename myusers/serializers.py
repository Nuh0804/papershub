from djoser.serializers import UserCreateSerializer, UserSerializer
   

class UserCreaterSerializer(UserCreateSerializer):
   class Meta(UserCreateSerializer.Meta):
      fields = ['id', 'username', 'password', 'email', 'first_name', 'last_name', 'phone_number', 'degree_program']

class CurrentUserSerializer(UserSerializer):
   class Meta(UserSerializer.Meta):
      fields = ['email', 'id','first_name', 'last_name', 'degree_program', 'year', 'subscribed']
      

