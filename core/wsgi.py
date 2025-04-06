"""
WSGI config for core project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from django.conf import settings
import pydevd_pycharm

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
if settings.DEBUG:
    pydevd_pycharm.settrace('host.docker.internal', port=5680, stdoutToServer=True, stderrToServer=True, suspend=False)

application = get_wsgi_application()
