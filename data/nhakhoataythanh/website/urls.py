from django.urls import path
from .views import home,about,service,pricing,blog,blog_details,contact
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home, name='home'),
    path('about', about, name='about'),
    path('service', service, name='service'),
    path('pricing', pricing, name='pricing'),
    path('blog', blog, name='blog'),
    path('blogdetails/', blog_details, name='blog_details'),
    path('blogdetails/<str:pk>/', blog_details, name='blog_details'),
    path('contact', contact, name='contact'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)