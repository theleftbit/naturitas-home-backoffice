# coding=utf-8
from .base import *

DEBUG = False

ADMINS = [('Admin', 'sysadmin@visual-engin.com')]

ALLOWED_HOSTS = [API_DOMAIN]

CSRF_TRUSTED_ORIGINS = ['.naturitas.com']

# Enabling CORS
CORS_ORIGIN_ALLOW_ALL = True

CORS_ALLOW_HEADERS = (
    'accept',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
)
