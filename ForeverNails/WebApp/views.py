from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post
from .covid_form import PostForm


def Main(request):
    return render(request, 'blog/Main.html', {})


def Menu(request):
    return render(request, 'blog/Menu.html', {})

def boot(request):
    return render(request, 'blog/boot.html', {})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
    form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})



