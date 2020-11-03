from django.contrib import admin
from .models import Post
from .models import Profile
from django.contrib.auth.models import User

admin.site.register(Post)
admin.site.register(Profile)
#user = User.objects.create_user('myusername', 'myemail@email.com', 'mypassword')

#user.first_name = 'Kin'
#user.lastname = "Lo"
#user.save()
