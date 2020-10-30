from __future__ import unicode_literals
from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import *
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
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(default="", max_length=200)
    last_name = models.CharField(default="", max_length=200)
    email = models.EmailField(default="", max_length=200)
    phone_number = models.IntegerField(default="", editable=True)
    birth_date = models.DateField(null=True, blank=True)

    def create_user_Profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user_name=instance)
            post_save.connect(create_user_profile, sender=User)
    def save_user_Profile(sender, instance, **kwargs):
        instance.profile.save()

    def __str__(self):
        return f"{self.first_name},{self.last_name},{self.email},{self.phone_number}, {self.birth_date}"


class appointManager(models.Manager):
    def appointval(self, postData, id):
        errors = []
        print(postData["time"])
        print(datetime.now().strftime("%H:%M"))
        if postData['date']:
            if not postData["date"] >= unicode(date.today()):
                errors.append("Date must be set in future!")
            if len(postData["date"]) < 1:
                errors.append("Date field can not be empty")
            print("got to appointment post Data:", postData['date'])
        if len(Appointment.objects.filter(date = postData['date'] ,time= postData['time'])) > 0:
            errors.append("Can Not create an appointment on existing date and time")
        if len(postData['task'])<2:
            errors.append("Please insert take, must be more than 2 characters")
        if len(errors)==0:
            makeappoint= Appointment.objects.create(user=User.objects.get(id=id), task= postData['task'],date= str(postData['date']),time= postData['time'])
            return(True, makeappoint)
        else:
            return(False, errors)

    def edit_appointment(self, postData, app_id):
        errors = []
        print(errors)
        # if postData['edit_date']:
        if not postData["edit_date"] >= unicode(date.today()):
            errors.append("Appointment date can't be in the past!")
            print("appoint date can't be past")
        if postData["edit_date"] == "" or len(postData["edit_tasks"]) < 1:
            errors.append("All fields must be filled out!")
            print("all fields must fill out pop out")
        if errors == []:
            update_time= self.filter(id = app_id).update(task = postData['edit_tasks'], status = postData['edit_status'],
                                                         time = postData['edit_time'], date = postData['edit_date'])

            return (True, update_time)
        else:
            return (False, errors)


class Appointment(models.Model):
    service_choices = (
        ("NF", "Solar Full Set"),
        ("NFR", "Solar Refill"),
        ("NPW", "Solar P&W Full Set"),
        ("NPF", "Solar P&W Refill"),
        ("NPC", "Powder Color Full Set"),
        ("NPR", "Powder Refill"),
        ("M", "Manicure Shellac"),
        ("P", "Pedicure Shellac"),
        ("W", "Waxing"),
        ("F", "Facial"),
        ("E", "Eyelashes"),
        ("M", "Massage"),
        ("T", "Permanent Tattoo"),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    service_choices = models.CharField(max_length=100, choices=service_choices)
    status = models.CharField(max_length=255)
    date = models.DateField(blank=True, null=True)
    time = models.TimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    objects = appointManager()




