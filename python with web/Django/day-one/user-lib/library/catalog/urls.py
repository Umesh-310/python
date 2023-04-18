from django.urls import path
from .views import index_view, BookCreate, BookDetail

urlpatterns = [
    path('', index_view, name='index'),
    path('create_book/', BookCreate.as_view(), name='create_book'),
    path('book/<int:pk>', BookDetail.as_view(), name='book_detail')

]
