from django.contrib.auth.models import User
from rest_framework import serializers
from .models import UserProfile

# This is working Good
class UserProfileSerializer(serializers.ModelSerializer, serializers.Serializer):
    username = serializers.CharField(source='user.username')
    email = serializers.EmailField(source='user.email')
    first_name = serializers.CharField(source='user.first_name')
    last_name = serializers.CharField(source='user.last_name')
    age = serializers.IntegerField()
    gender = serializers.CharField()

    class Meta:
        model = UserProfile
        fields = ('id', 'username', 'email', 'first_name',
                  'last_name', 'age', 'gender')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name',
                  'email', 'is_staff', 'is_active', 'date_joined')


# class UserProfileSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ('id', 'username', 'email', 'first_name', 'last_name')
