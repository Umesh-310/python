from django.urls import path
from .views import add, list, delete

app_name = 'cars'

urlpatterns = [
    path('add/', add, name='add'),
    path('delete/', delete, name='delete'),
    path('list/', list, name='list'),
]
