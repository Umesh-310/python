from .forms import UserProfileLoginForm
from django.contrib.auth import login
from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from .models import UserProfile
# from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .serializers import UserProfileSerializer, UserProfileSerializer, UserSerializer, User


class UserProfileList(generics.ListCreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


class UserProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


def login_view(request):
    form = UserProfileLoginForm(request.POST or None)
    if form.is_valid():
        user_profile = form.cleaned_data['user_profile']
        login(request, user_profile)
        return {'Message': "Done"}

    context = {'form': form}
    return render(request, 'registration/login.html', context)


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
