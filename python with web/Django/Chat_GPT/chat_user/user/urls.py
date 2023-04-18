from django.urls import path
from . import views

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('user/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('user/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('user-profiles/', views.UserProfileList.as_view(),
         name='user_profile_list'),
    path('user-profiles/<int:pk>/', views.UserProfileDetail.as_view(),
         name='user_profile_detail'),
    path('login/', views.login_view, name='login'),
    path('users/', views.UserList.as_view(), name='user-list'),
]
