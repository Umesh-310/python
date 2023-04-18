from django.contrib import admin
from .models import UserAdd, UserDetails
# Register your models here.

admin.site.register(UserDetails)
admin.site.register(UserAdd)
