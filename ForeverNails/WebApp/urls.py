from django.urls import path
from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.Main, name='Main'),
    path('Home', views.Main, name='Main'),
    path('ServiceMenu', views.Menu, name='Menu'),
    path('Contact', views.Contact, name='Contact'),
    path('location', views.location, name='location'),
    path('gallery', views.Gallery, name='Gallery'),
    path('login', views.LogIN, name='login'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('register', views.register, name='register'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
]
