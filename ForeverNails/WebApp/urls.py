from django.urls import path
from . import views


urlpatterns = [
    path('', views.Main, name='Main'),
    path('Home', views.Main, name='Main'),
    path('ServiceMenu', views.Menu, name='Menu'),
    path('Contact', views.Contact, name='Contact'),
    path('location', views.location, name='location'),
    path('boot', views.boot, name='boot'),
    path('login', views.LogIN, name='login'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
]
