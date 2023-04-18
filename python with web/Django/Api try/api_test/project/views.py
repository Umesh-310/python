from django.contrib.auth.models import User
from .serializers import RegisterSerializer
from rest_framework import generics
from rest_framework.permissions import AllowAny

from django.shortcuts import render
from django.views.generic import CreateView
from .models import Student
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required
def studentInfo(request, ):

    info = Student.admin_objects.all().count()

    return render(request, 'project/studentInfo.html', context={'info': info})


class FromCreate(CreateView):
    model = Student

    fields = '__all__'

    success_url = ''


class RegisterView(generics.CreateAPIView):
    # queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer
