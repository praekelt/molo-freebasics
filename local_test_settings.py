from freebasics.settings import *  # noqa

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'freebasics_test.db',
    }
}

DEBUG = True
CELERY_ALWAYS_EAGER = True
