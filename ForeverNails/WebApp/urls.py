from django.urls import path
from django.conf import settings
from . import views
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings


urlpatterns = [
    path('', views.main, name='Main'),
    path('Home', views.main, name='Main'),
    path('ServiceMenu', views.menu, name='Menu'),
    path('Contact', views.contact, name='Contact'),
    path('location', views.location, name='Location'),
    path('gallery', views.gallery, name='Gallery'),
    path('login', views.LogIN, name='login'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('register', views.register, name='register'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('profile', views.update_profile, name='profile'),
    path('scheduler', views.scheduler, name='scheduler'),
]
