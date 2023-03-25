from django.urls import path
from . import views
app_name = 'my_app'
urlpatterns = [
    path('', views.example, name='example'),
    path('variable/', views.variable_view , name='variable')
]
