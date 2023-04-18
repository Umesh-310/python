from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

urlpatterns = [
    path('token/', views.CustomTokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('create/', views.UserDetail.as_view()),
    path('user-profile', views.UserDetailUpdate.as_view()),
    path('<str:email>', views.UserGiveAToken),
]
