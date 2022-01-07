from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from base import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('base.urls')),
    path('api/', include('base.api.urls')),
    # Upload pictures
    path('upload_image/', views.upload_image)
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
