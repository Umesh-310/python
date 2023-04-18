from django.db import models

from django import forms
from django.contrib.auth.models import User

from django.db import models

# Create your models here.


class StudentManager(models.Manager):

    def get_queryset(self):
        return super().get_queryset().filter()(is_deleted=False)


class Student(models.Model):

    userName = models.CharField(max_length=50)
    className = models.CharField(max_length=20)
    age = models.IntegerField(null=True)
    is_deleted = models.BooleanField(default=False)
    studentDetails = models.TextField(null=True, blank=True)
    
    objects = StudentManager()
    admin_objects = models.Manager()

    def __str__(self) -> str:
        return self.userName
