from django.urls import path
from .views import studentInfo, FromCreate


urlpatterns = [
    path('student/', studentInfo, name='student'),
    path('addNew/', FromCreate.as_view(), name='add_student'),
]
