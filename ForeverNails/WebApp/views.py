from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post
from .covid_form import PostForm
from django.contrib.auth import logout, authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.views.generic import TemplateView
from braces.views import LoginRequiredMixin
from .form import *

def Main(request):
    return render(request, 'index/Main.html', {})

def Menu(request):
    return render(request, 'index/Menu.html', {})

def LogIN(request):
    return render(request, 'registration/login.html', {})

def Contact(request):
    return render(request, 'index/Contact.html', {})

def Gallery(request):
    return render(request, 'index/gallery.html', {})

def location(request):
    return render(request, 'index/location.html', {})

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

            return render(request = request,
                          template_name = "index/register.html",
                          context={"form":form})

    form = UserCreationForm
    return render(request = request,
                  template_name = "index/register.html",
                  context={"form":form})

def Profile(request):
    return render(request, 'index/profile.html', {})

def update_profile(request, user_id):
    user = User.objects.get(pk=user_id)
    user.save()

class ProfileUpdateView(LoginRequiredMixin, TemplateView):
    user_form = UserForm
    profile_form = ProfileForm
    template_name = 'base.html'

    def post(self, request):

        post_data = request.POST or None

        user_form = UserForm(post_data, instance=request.user)
        profile_form = ProfileForm(post_data, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your Profile has been Successfully Updated!')
            return HttpResponseRedirect(reverse_lazy('profile'))

        context = self.get_context_data(
            user_form=user_form,
            profile_form=profile_form
        )

        return self.render_to_response(context)

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'index/post_detail.html', {'post': post})

def post_new(request):
    form = PostForm()
    return render(request, 'index/post_edit.html', {'form': form})

