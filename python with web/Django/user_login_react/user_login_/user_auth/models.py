from django.contrib.auth.models import User
from django.db import models


# class UserAddress(models.Model):
#     _state = models.


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    DOB = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=10, null=True, blank=True)
    phone = models.IntegerField(null=True, blank=True)
    about_self = models.TextField(null=True, blank=True)
    # address = models.OneToOneField()

    def __str__(self) -> str:
        return f"{self.user}"


class Image(models.Model):
    p_image = models.ImageField(upload_to='images/', null=True, blank=True)
    # image = models.TextField(null=True, blank=True)
    user_i = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.user_i.username} Profile Image"


class UserAdd(models.Model):
    city = models.CharField(max_length=150, null=True, blank=True)
    state = models.CharField(max_length=150, null=True, blank=True)
    # pincode = models.IntegerField()
    user_a = models.ForeignKey(User, on_delete=models.CASCADE)
    # user = models

    def __str__(self) -> str:
        return f"{self.user_a.username} {self.city}"
