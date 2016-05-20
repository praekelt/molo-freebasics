"""
Django settings for base freebasics.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

from os.path import abspath, dirname, join
from os import environ
from django.conf import global_settings
from django.utils.translation import ugettext_lazy as _
import dj_database_url
from celery.schedules import crontab

# Absolute filesystem path to the Django project directory:
PROJECT_ROOT = dirname(dirname(dirname(abspath(__file__))))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "+qjha14e^w1+41tqi$fhc=y(%iijt&q)0mw@kze!ewz)7($#4#"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Base URL to use when referring to full URLs within the Wagtail admin
# backend - e.g. in notification emails. Don't include '/admin' or
# a trailing slash
BASE_URL = 'http://example.com'


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django_extensions',

    'taggit',
    'modelcluster',
    'overextends',

    'molo.core',
    'freebasics',

    'wagtail.wagtailcore',
    'wagtail.wagtailadmin',
    'wagtail.wagtaildocs',
    'wagtail.wagtailsnippets',
    'wagtail.wagtailusers',
    'wagtail.wagtailsites',
    'wagtail.wagtailimages',
    'wagtail.wagtailembeds',
    'wagtail.wagtailsearch',
    'wagtail.wagtailredirects',
    'wagtail.wagtailforms',
    'wagtailmodeladmin',
    'wagtail.contrib.settings',

    'mptt',
    'molo.profiles',
    'django_comments',
    'molo.commenting',
    'molo.polls',

    'raven.contrib.django.raven_compat',
    'django_cas_ng',
    'compressor',
]

COMMENTS_APP = 'molo.commenting'
COMMENTS_FLAG_THRESHHOLD = 3
COMMENTS_HIDE_REMOVED = False

SITE_ID = 1

MIDDLEWARE_CLASSES = [
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'wagtail.wagtailcore.middleware.SiteMiddleware',
    'wagtail.wagtailredirects.middleware.RedirectMiddleware',
    'wagtailmodeladmin.middleware.ModelAdminMiddleware',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'molo.core.context_processors.locale',
                'molo.profiles.context_processors.get_profile_data',
                'wagtail.contrib.settings.context_processors.settings',
            ],
            'builtins': ['overextends.templatetags.overextends_tags'],
        },
    },
]

ROOT_URLCONF = 'freebasics.urls'
WSGI_APPLICATION = 'freebasics.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

# SQLite (simplest install)
DATABASES = {'default': dj_database_url.config(
    default='sqlite:///%s' % (join(PROJECT_ROOT, 'db.sqlite3'),))}

# PostgreSQL (Recommended, but requires the psycopg2 library and Postgresql
#             development headers)
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'base',
#         'USER': 'postgres',
#         'PASSWORD': '',
#         'HOST': '',  # Set to empty string for localhost.
#         'PORT': '',  # Set to empty string for default.
#         # number of seconds database connections should persist for
#         'CONN_MAX_AGE': 600,
#     }
# }

CELERY_IMPORTS = ('molo.core.tasks')
BROKER_URL = environ.get('BROKER_URL', 'redis://localhost:6379/0')
CELERY_RESULT_BACKEND = environ.get(
    'CELERY_RESULT_BACKEND', 'redis://localhost:6379/0')
CELERY_ACCEPT_CONTENT = ['json']

CELERYBEAT_SCHEDULE = {
    'rotate_content': {
        'task': 'molo.core.tasks.rotate_content',
        'schedule': crontab(minute=0),
    },
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-gb'
TIME_ZONE = 'Africa/Johannesburg'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Native South African languages are currently not included in the default
# list of languges in django
# https://github.com/django/django/blob/master/django/conf/global_settings.py#L50
LANGUAGES = global_settings.LANGUAGES + [
    ('zu', _('Zulu')),
    ('xh', _('Xhosa')),
    ('st', _('Sotho')),
    ('ve', _('Venda')),
    ('tn', _('Tswana')),
    ('ts', _('Tsonga')),
    ('ss', _('Swati')),
    ('nr', _('Ndebele')),
]

LOCALE_PATHS = [
    join(PROJECT_ROOT, "locale"),
]

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_ROOT = join(PROJECT_ROOT, 'static')
STATIC_URL = '/static/'

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
]

MEDIA_ROOT = join(PROJECT_ROOT, 'media')
MEDIA_URL = '/media/'


# Django compressor settings
# http://django-compressor.readthedocs.org/en/latest/settings/

COMPRESS_PRECOMPILERS = [
    ('text/x-scss', 'django_libsass.SassCompiler'),
]


# Wagtail settings
LOGIN_URL = 'wagtailadmin_login'
LOGIN_REDIRECT_URL = 'wagtailadmin_home'

WAGTAIL_SITE_NAME = "base"

# Use Elasticsearch as the search backend for extra performance and better
# search results:
# http://wagtail.readthedocs.org/en/latest/howto/performance.html#search
# http://wagtail.readthedocs.org/en/latest/core_components/
#     search/backends.html#elasticsearch-backend
#
# WAGTAILSEARCH_BACKENDS = {
#     'default': {
#         'BACKEND': ('wagtail.wagtailsearch.backends.'
#                     'elasticsearch.ElasticSearch'),
#         'INDEX': 'base',
#     },
# }


# Whether to use face/feature detection to improve image
# cropping - requires OpenCV
WAGTAILIMAGES_FEATURE_DETECTION_ENABLED = False

ENABLE_SSO = False
CUSTOM_CSS_BASE_BACKGROUND_COLOR = environ.get(
    'CUSTOM_CSS_BASE_BACKGROUND_COLOR', "#ffffff")
CUSTOM_CSS_BODY_FONT_FAMILY = environ.get(
    'CUSTOM_CSS_BODY_FONT_FAMILY', "Arial, Helvetica, sans-serif")
CUSTOM_CSS_BLOCK_BACKGROUND_COLOR = environ.get(
    'CUSTOM_CSS_BLOCK_BACKGROUND_COLOR', "#dfdfdf")
CUSTOM_CSS_BLOCK_FONT_FAMILY = environ.get(
    'CUSTOM_CSS_BLOCK_FONT_FAMILY', "Arial, Helvetica, sans-serif")
CUSTOM_CSS_BLOCK_TEXT_TRANSFORM = environ.get(
    'CUSTOM_CSS_BLOCK_TEXT_TRANSFORM', "uppercase")
CUSTOM_CSS_ACCENT_1 = environ.get('CUSTOM_CSS_ACCENT_1', "#69269d")
CUSTOM_CSS_ACCENT_2 = environ.get('CUSTOM_CSS_ACCENT_2', "#c736c0")

SITE_NAME = environ.get('SITE_NAME', "Molo Free Basics")
WAGTAIL_SITE_NAME = SITE_NAME

BLOCK_POSITION_BANNER = int(environ.get('BLOCK_POSITION_BANNER', 1))
BLOCK_POSITION_LATEST = int(environ.get('BLOCK_POSITION_LATEST', 2))
BLOCK_POSITION_QUESTIONS = int(environ.get('BLOCK_POSITION_QUESTIONS', 3))
BLOCK_POSITION_SECTIONS = int(environ.get('BLOCK_POSITION_SECTIONS', 4))

UNICORE_DISTRIBUTE_API = 'http://localhost:6543'

ADMIN_LANGUAGE_CODE = environ.get('ADMIN_LANGUAGE_CODE', "en")
