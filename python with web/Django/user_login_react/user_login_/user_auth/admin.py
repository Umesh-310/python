from django.contrib import admin
from .models import UserProfile, UserAdd, Image
# Register your models here.

admin.site.register(UserProfile)
admin.site.register(UserAdd)
admin.site.register(Image)