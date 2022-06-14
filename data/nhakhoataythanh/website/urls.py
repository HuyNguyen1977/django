from django.urls import path
from . import views
from .views import home,service,pricing,blog,blog_details,contact
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home, name='home'),
    path('qa', views.qa, name='qa'),
    path('service', service, name='service'),
    path('pricing', pricing, name='pricing'),
    # path('blog', blog, name='blog'),
    path('blogdetails/', blog, name='blog'),
    path('blogdetails/<str:pk>/', blog_details, name='blog_details'),
    path('contact', contact, name='contact'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)