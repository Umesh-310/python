from django.urls import path
from .views import allData, addProduct, allUser, ProductCreate, UserAddCreate, UserCreate
urlpatterns = [
    path('product/', allData, name='AllData'),
    path('user/', allUser, name='AllUser'),
    path('addProduct/', addProduct),
    path("add/", ProductCreate.as_view()),
    path("adduseradd/", UserAddCreate.as_view()),
    path("adduser/", UserCreate.as_view()),
]
