from django.urls import path
from . import views

urlpatterns = [
    path("", views.simple_view)
]


# urlpatterns = [
#     path('<int:num_page>/', views.page_num),
#     path('<topic>/', views.sports_page, name='topic-page'),
#     path('<int:num1>/<int:num2>', views.add_view),
#     # path('news', views.news_page),
# ]
