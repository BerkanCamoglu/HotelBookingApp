from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from .views import *
urlpatterns = [
    path("", home,name='home'),
    path("hotel-detail/<uid>/",hotel_detail,name ="hotel_detail"),
    path("login/", login_page,name='login_page'),
    path("register/", register_page,name='register_page'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)