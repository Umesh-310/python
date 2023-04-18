from django.urls import path
from . import views

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('user/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('user/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('user/', views.addStudentname, name='token_obtain_pair'),
    path('user-profiles/', views.UserProfileList.as_view(),
         name='user_profile_list'),
    path('user-profiles/<int:pk>/', views.UserProfileDetail.as_view(),
         name='user_profile_detail'),
    #     path('user/<int:pk>/', views.UserDetail.as_view(),
    #     name='user_detail'),
    path('user-all/<int:pk>/', views.MultiCreateAPIView.as_view(), name="userAll"),
    path('user-add/', views.UserSignUpView.as_view(), name="userAdd"),
    path('email/', views.sendMail, name="email"),
    path('otp/', views.checkOtp, name="otp"),
]
