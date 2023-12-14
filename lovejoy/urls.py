
from django.contrib import admin
from django.urls import path, include

#import settings
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('evaluation.urls',namespace='evaluation')),
]   + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
