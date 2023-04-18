from django.urls import path
from .views import deleteStd, updateStd, userData, getStudent, getStudents, addStudentname
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from project.views import RegisterView


urlpatterns = [
    path('user/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('user/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view(), name='auth_register'),

    path('user/', userData, name='user'),
    path('students/', getStudents, name='serializers'),
    path('student/<int:pk>', getStudent, name='serializer'),
    path('addStd/', addStudentname),
    path('delete/', deleteStd),
    path('update/', updateStd)
]
