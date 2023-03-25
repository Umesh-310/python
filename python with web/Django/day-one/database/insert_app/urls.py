from django.urls import path
from .views import list_student

urlpatterns = [
    path("", list_student, name='list_student')
]
