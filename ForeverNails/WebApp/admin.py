from django.contrib import admin
from .models import Post
from .models import Profile
from .models import Appointment
from django.contrib.auth.models import User

admin.site.register(Post)
admin.site.register(Profile)
admin.site.register(Appointment)
