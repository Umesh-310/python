from django.db import models
from app_data.models import AddProduct , User
import uuid

# Create your models here.


class UserDetails(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user_profile_pic = models.FileField()
    user_name = models.CharField(max_length=100)
    user_mobile_number = models.IntegerField()

    user_address = models.ForeignKey(
        'UserAdd', related_name="user_address", null=True, blank=True, on_delete=models.SET_NULL)

    user = models.ForeignKey(User, related_name='user',
                             on_delete=models.CASCADE)

    user_products = models.ForeignKey(AddProduct, related_name='user_products',
                                      null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self) -> str:
        return self.user_name


class UserAdd(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user_city = models.CharField(max_length=150)
    user_state = models.CharField(max_length=150)
    user_pincode = models.IntegerField(default=458664)

    def __str__(self) -> str:
        return f"{self.user_city}"
