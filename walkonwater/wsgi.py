"""
WSGI config for walkonwater project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os
import logging

from django.core.wsgi import get_wsgi_application


logger = logging.getLogger(__name__)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "walkonwater.settings")

django_application = get_wsgi_application()

try:
    import uwsgi
except ImportError as error:
    uwsgi = None
    logging.debug('uWSGI is not available')


def application(environ, start_response):
    return django_application(environ, start_response)