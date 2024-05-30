from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('vr.html', views.vr, name='vr'),
    path('kz.html', views.kz),
    path('gallery.html', views.gallery),
    path('about.html', views.about),
    path('contact.html', views.contact),
    path('index.html', views.index),
    

]
