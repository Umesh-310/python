from django.urls import path
from .views import ImageFile
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('all/', ImageFile.as_view()),
]
# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
