from os import environ

import dj_database_url

from .production import *


# Disable debug mode

DEBUG = False
TEMPLATE_DEBUG = False

SECRET_KEY = environ.get('SECRET_KEY') or 'please-change-me'
PROJECT_ROOT = (
    environ.get('PROJECT_ROOT') or dirname(dirname(abspath(__file__))))

RAVEN_DSN = environ.get('RAVEN_DSN')
RAVEN_CONFIG = {'dsn': RAVEN_DSN} if RAVEN_DSN else {}

CAS_SERVER_URL = environ.get('CAS_SERVER_URL') or ''
UNICORE_DISTRIBUTE_API = environ.get('UNICORE_DISTRIBUTE_API') or ''
FROM_EMAIL = environ.get('FROM_EMAIL', "support@moloproject.org")
CONTENT_IMPORT_SUBJECT = environ.get(
    'CONTENT_IMPORT_SUBJECT', 'Molo Content Import')

COMPRESS_OFFLINE = True

DATABASES = {
    'default': dj_database_url.config(
        default='sqlite:///%s' % (join(PROJECT_ROOT, 'molo.db'),))}

MEDIA_ROOT = join(PROJECT_ROOT, 'media')

STATIC_ROOT = join(PROJECT_ROOT, 'static')

LOCALE_PATHS = (
    join(PROJECT_ROOT, "locale"),
)
