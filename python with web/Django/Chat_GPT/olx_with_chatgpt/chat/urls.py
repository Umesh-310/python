from django.urls import path
from . import views

urlpatterns = [
    path('categories/', views.CategoryList.as_view()),
    path('listings/', views.ListingList.as_view()),
    path('listings/<int:pk>/', views.ListingDetail.as_view()),
    path('images/', views.ImageList.as_view()),
    path('images/<int:pk>/', views.ImageDetail.as_view()),
    path('messages/', views.MessageList.as_view()),
    path('messages/<int:pk>/', views.MessageDetail.as_view()),
    path('transactions/', views.TransactionList.as_view()),
    path('transactions/<int:pk>/', views.TransactionDetail.as_view()),
    path('reviews/', views.ReviewList.as_view()),
    path('reviews/<int:pk>/', views.ReviewDetail.as_view()),
    path('categories/create/', views.CategoryCreate.as_view(),
         name='category-create'),
    path('listings/create/', views.ListingCreate.as_view(), name='listing-create'),

]
