from django.urls import path
from .views import ImageUpload ,UploadView

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('all/', ImageUpload.as_view()),
    path('upload-image/', UploadView.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
