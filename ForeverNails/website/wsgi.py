"""
WSGI config for website project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""


from django.core.wsgi import get_wsgi_application
from django.contrib.staticfiles.handlers import StaticFilesHandler
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'website.settings')

application = StaticFilesHandler(get_wsgi_application())
