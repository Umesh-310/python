from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    p_image = models.CharField(max_length=200, null=True, blank=True)
    otp = models.IntegerField(null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.user} {self.id}"
