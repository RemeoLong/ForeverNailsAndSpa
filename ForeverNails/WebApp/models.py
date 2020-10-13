from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Employee(models.Model):
    skills_choices = (
        ("NF", "Solar Full Set"),
        ("NPW", "Solar P&W Full Set"),
        ("NPC", "Powder Color Full Set"),
        ("M", "Manicure Shellac"),
        ("P", "Pedicure Shellac"),
        ("W", "Waxing"),
        ("F", "Facial"),
        ("E", "Eyelashes"),
        ("M", "Massage"),
        ("T", "Permanent Tattoo"),
    )
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    phone_number = models.IntegerField(default="", editable=False)
    skills = models.CharField(max_length=100, choices=skills_choices)
    clock_in = models.DateTimeField(default=timezone.now)
    clock_out = models.DateTimeField(default=timezone.now)
    active = models.BooleanField(default=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.first_name) + str(self.last_name)


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone_number = models.IntegerField(default="", editable=True)
    birth_date = models.DateTimeField(null=True, blank=True)

    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

    def __str__(self):
        return f"{self.phone_number}, {self.birth_date}"






