from django import forms
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth.forms import UserChangeForm


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
        }


class UserUpdateForm(UserForm, UserChangeForm):
    first_name = forms.CharField(
        required=True, widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    last_name = forms.CharField(
        required=True, widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    email = forms.EmailField(
        required=True, widget=forms.TextInput(attrs={'class': 'form-control'})
    )


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('phone_number', 'birth_date')
        widgets = {
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'birth_date': forms.TextInput(attrs={'class': 'form-control'}),
        }


class ProfileUpdateForm(ProfileForm, UserChangeForm):
    phone_number = forms.IntegerField(
        required=True, widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    birth_date = forms.CharField(
        required=True, widget=forms.TextInput(attrs={'class': 'form-control'})
    )


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ('provider', 'services', 'date', 'time', 'comments')
        widgets = {
            'provider': forms.MultipleChoiceField(required=False, widget=forms.CheckboxSelectMultiple,
                                                  choices=[("Linh / Sugar", "Linh"), ("Mia", "Hien"),
                                                           ("Jennifer", "Nhung"), ("Theresa", "Cho Dung")]),
            'services': forms.MultipleChoiceField(required=True, widget=forms.CheckboxSelectMultiple,
                                                  choices=[("Nails Solar Full Set", "NF"), ("Solar P&W Full Set", "NWP"),
                                                           ("Powder Color Full Set", "NPC"), ("Manicure Regular", "MR"),
                                                           ("Manicure Shellac", "MS"), ("Pedicure Regular", "PR"),
                                                           ("Pedicure Shellac", "PS"), ("Waxing", "W"), ("Facial", "F"),
                                                           ("Eyelashes", "E"), ("Massage", "M"),
                                                           ("Permanent Tattoo", "T")]),
            'date': forms.DateField(required=True, widget=forms.DateInput),
            'time': forms.TimeField(required=True, widget=forms.TimeInput),
            'comments': forms.TextInput(),
        }
