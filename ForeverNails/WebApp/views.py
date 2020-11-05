from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post
from .covid_form import PostForm
from django.contrib.auth import logout, authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.views.generic import TemplateView
from .form import *
from django.contrib.auth.decorators import login_required
from django.db import transaction


def main(request):
    return render(request, 'index/Main.html', {})


def menu(request):
    return render(request, 'index/Menu.html', {})


def LogIN(request):
    return render(request, 'registration/login.html', {})


def contact(request):
    return render(request, 'index/Contact.html', {})


def gallery(request):
    return render(request, 'index/gallery.html', {})


def location(request):
    return render(request, 'index/location.html', {})


def scheduler(request):
    return render(request, 'index/scheduler.html', {})


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            login(request, user)
            return redirect("/profile")

        else:
            for msg in form.error_messages:
                print(form.error_messages[msg])

            return render(request=request,
                          template_name="index/register.html",
                          context={"form": form})

    form = UserCreationForm
    return render(request=request,
                  template_name="index/register.html",
                  context={"form": form})


@login_required(login_url="/Home")
@transaction.atomic
def update_profile(request):
    if request.method == "POST":
        u_form = UserForm(request.POST, instance=request.user)
        p_form = ProfileForm(request.POST, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'Your profile was successfully updated!')
            return redirect('profile')
        else:
            messages.error(request, _('Please correct the error below'))
    else:
        u_form = UserForm
        p_form = ProfileForm
    return render(request, 'index/profile.html', {
        'u_form': u_form,
        'p_form': p_form
    })


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'index/post_detail.html', {'post': post})


def post_new(request):
    form = PostForm()
    return render(request, 'index/post_edit.html', {'form': form})
