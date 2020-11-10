from django import forms
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth.forms import UserChangeForm
import datetime


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
        }


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('phone_number', 'birth_date')
        widgets = {
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'birth_date': forms.TextInput(attrs={'class': 'form-control'}),
        }


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ('provider', 'services', 'date', 'time', 'comments')
        widgets = {
            'date': forms.DateInput(format='%d/%m/%y'),
            'time': forms.TimeInput(format='%H:%M'),
            'comments': forms.TextInput(attrs={'class': 'form-control'}),
        }