from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import *
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
            messages.error(request, 'Please correct the error below')
    else:
        u_form = UserForm
        p_form = ProfileForm
    return render(request, 'index/profile.html', {
        'u_form': u_form,
        'p_form': p_form
    })


@login_required(login_url="/Home")
@transaction.atomic
def scheduler(request):
    if request.method == "POST":
        a_form = AppointmentForm(request.POST, instance=request.user) #<<< issues here >>>#
        if a_form.is_valid():
            a_form.save()
 #           a_form.save(commit=False)
 #           makeappt = Appointment.objects.create(user=User.objects.get(id=id), provider=postData['provider'],
  #                                                services=postData['services'], date=str(postData['date']),
 #                                                 time=postData['time'])
 #           a_form.save(commit)
            messages.success(request, 'Your Appointment was successfully updated!')
            return redirect('scheduler')
        else:
            messages.error(request, 'Please correct the error below')
    else:
        a_form = AppointmentForm
    return render(request, 'index/scheduler.html', {
        'a_form': a_form,
    })


def update(request, appoint_id):
    try:
        appointment = Appointment.objects.get(id=appoint_id)
    except Appointment.DoesNotExist:
        messages.info(request, "Appointment Not Found")
        return redirect('scheduler')

    context = {
        "appointment": appointment,
    }
    return render(request, 'index/scheduler.html', context)


def edit_appoint(request, appoint_id):
    if 'id' not in request.session:
        return redirect('/')
    if request.method != 'POST':
        messages.info(request, "Cannot edit like this!")
        return redirect('/update' + appoint_id)

    try:
        print("/")
        update_app = Appointment.objects.edit_appointment(request.POST, appoint_id)
        print("got to edit_appoint Try")
    except Appointment.DoesNotExist:
        messages.info(request,"appointment Not Found")
        return redirect('/update/'+appoint_id)
    if not update_app[0]:
        messages.info(request, "Please fill in all the spaces and make sure it's valid!")
        return redirect('/update/'+appoint_id)
    else:
        messages.success(request, "Successfully Updated Appointment")
        return redirect('scheduler')


def delete(request, appoint_id):
    try:
        target = Appointment.objects.get(id=appoint_id)
    except Appointment.DoesNotExist:
        messages.info(request, "Message Not Found")
        return redirect('scheduler')
    target.delete()
    return redirect('scheduler')


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'index/post_detail.html', {'post': post})


def post_new(request):
    form = PostForm()
    return render(request, 'index/post_edit.html', {'form': form})
