from django.contrib import admin
from django.urls import path, include
from django.conf import settings            # buranı əlavə et
from django.conf.urls.static import static  # buranı əlavə et

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('guvenluxapp.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)