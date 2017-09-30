# -*- coding: utf-8 -*-
from . import *

# django-nose settings

INSTALLED_APPS += (
    'django_nose',
)

# REST_FRAMEWORK['TEST_REQUEST_RENDERER_CLASSES'] = (
#     'apps.manager.api.renderers.JSONRenderer',
# )
# REST_FRAMEWORK['TEST_REQUEST_DEFAULT_FORMAT'] = (
#     'application/vnd.api+json',
# )

REST_FRAMEWORK['PAGE_SIZE'] = 10
REST_FRAMEWORK['DEFAULT_PERMISSION_CLASSES'] = 'rest_framework.permissions.AllowAny',

TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

NOSE_ARGS = [
    '--with-coverage',
    '--cover-package=apps.am_auth_api,apps.core,apps.logger,apps.manager,apps.media_platforms',
    '--cover-inclusive',
    '--cover-html',
    '--with-xunit',
    '--with-doctest',
    '--cover-xml',
    '--verbosity=1',
]

LOGGING['loggers']['factory'] = {
    'handlers': ['console'],
    'level': 'ERROR',
}

CELERY_ALWAYS_EAGER = True

TEST_DIRECTORY_SUFFIX = '_test'

MEDIA_ROOT += TEST_DIRECTORY_SUFFIX
