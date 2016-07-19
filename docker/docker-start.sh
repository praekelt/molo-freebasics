#!/bin/bash

set -e

# ensure we create the locales first so that Django doesn't complain
LANGUAGE_CODE=en ./manage.py compilemessages

./manage.py migrate --noinput
./manage.py collectstatic --noinput
./manage.py compress

echo "=> Starting nginx"
nginx; service nginx reload

echo "=> Starting Supervisord"
supervisord -c /etc/supervisord.conf

echo "=> Tailing logs"
tail -qF /var/log/supervisor/*.log
