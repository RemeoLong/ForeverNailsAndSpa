from django.urls import path
from . import views

urlpatterns = [
    path('', views.Main, name='Main'),
    path('ServiceMenu', views.Menu, name='Menu'),
    path('boot', views.boot, name='boot'),
    path('Log_In', views.LogIN, name='LogIN'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
]
