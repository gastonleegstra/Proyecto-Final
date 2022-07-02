from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from about.views import about

urlpatterns = [
    path('about/', about, name = 'about'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)