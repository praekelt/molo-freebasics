FROM praekeltfoundation/django-bootstrap:onbuild
RUN apt-get-install.sh git libjpeg-dev zlib1g-dev libffi-dev gettext libtiff-dev

ENV PROJECT_ROOT /app/
ENV DJANGO_SETTINGS_MODULE freebasics.settings.docker
ENV APP_MODULE "freebasics.wsgi:application"

ENV CELERY_APP freebasics
ENV CELERY_BEAT 1

RUN LANGUAGE_CODE=en ./manage.py compilemessages
RUN mkdir -p /app/media
RUN django-admin compress
RUN django-admin collectstatic --noinput
