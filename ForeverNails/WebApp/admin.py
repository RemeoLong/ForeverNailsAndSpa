from django.contrib import admin
from .models import Post
from django.contrib.auth.models import User

admin.site.register(Post)
#user = User.objects.create_user('myusername', 'myemail@email.com', 'mypassword')

#user.first_name = 'Kin'
#user.lastname = "Lo"
#user.save()
