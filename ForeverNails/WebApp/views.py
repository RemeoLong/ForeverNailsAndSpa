from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post
from .covid_form import PostForm
from django.contrib.auth import authenticate, login

def Main(request):
    return render(request, 'index/Main.html', {})

def Menu(request):
    return render(request, 'index/Menu.html', {})

def LogIN(request):
    return render(request, 'registration/login.html', {})

def Contact(request):
    return render(request, 'index/Contact.html', {})

def location(request):
    return render(request, 'index/location.html', {})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'index/post_detail.html', {'post': post})

def post_new(request):
    form = PostForm()
    return render(request, 'index/post_edit.html', {'form': form})



